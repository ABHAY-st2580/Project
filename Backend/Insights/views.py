from django.shortcuts import render
import pandas as pd
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import fpgrowth, association_rules
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from Sale.models import Sale, SaleItem
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from auth_api.models import Membership, Shop
from Tiles.models import Tile
import datetime
from django.utils import timezone
from datetime import date
from dateutil.relativedelta import relativedelta
from django.db.models import Sum
from collections import defaultdict

def get_user_shop(user):
    membership = Membership.objects.filter(user=user).first()
    return membership.shop if membership else None

def get_data(request):
    shop = get_user_shop(request.user)

    if not shop:
        return []
    sales = Sale.objects.filter(shop = shop)
    transactions = []

    for sale in sales:
        items = SaleItem.objects.filter(sale=sale)

        transaction = []

        for item in items:
            tile_type = item.tile_type or ''
            tile_name = item.tile_name_number or ''
            category = item.tile_type2 or ''

            combined = f"{tile_type}_{tile_name}_{category}".strip("_")

            if combined:
                transaction.append(combined)

        if transaction:
            transactions.append(transaction)

    return transactions

def encode_transactions(transactions):
    te = TransactionEncoder()
    te_array = te.fit_transform(transactions)
    df = pd.DataFrame(te_array, columns=te.columns_)
    return df

def run_fpgrowth(encoded_df, min_support=0.2, min_confidence=0.6):

    frequent_itemsets = fpgrowth(
        encoded_df,
        min_support=min_support,
        use_colnames=True
    )

    rules = association_rules(
        frequent_itemsets,
        metric="confidence",
        min_threshold=min_confidence
    )

    return frequent_itemsets, rules

@api_view(['POST'])
@permission_classes([IsAuthenticated])
@csrf_exempt
def get_recommendations(request):
    if request.method == "POST":
        data = json.loads(request.body)
        min_support = data.get("min_support", 0.2)
        min_confidence = data.get("min_confidence", 0.6)
        try:
            transactions = get_data(request)
            encoded = encode_transactions(transactions)
            _, rules = run_fpgrowth(encoded, min_support=min_support, min_confidence=min_confidence)

            result = []

            for _, row in rules.iterrows():
                result.append({
                    "if_bought": list(row['antecedents']),
                    "then_buy": list(row['consequents']),
                    "confidence": float(row['confidence'])
                })

            return JsonResponse({"rules": result})

        except Exception as e:
            return JsonResponse({"error": str(e)})
    else:
        return JsonResponse({"error": "Not a post request"})



@api_view(['GET'])
@permission_classes([IsAuthenticated])
@csrf_exempt
def debt(request):
    try:
        shop = get_user_shop(request.user)
        if not shop:
            return JsonResponse({"error": "User not linked to any shop"}, status=400)
        
        sales = Sale.objects.filter(shop = shop)

        data = []
        for sale in sales:
            if sale.remaining_amount > 0:
                data.append({
                    "customer_name": sale.customer_name,
                    "remaining_amount": sale.remaining_amount,
                    "date": str(sale.date),
                    "address": sale.address,
                    "phone_number": sale.phone_number
                })
        return JsonResponse({"debt": data})

    except Exception as e:
        return JsonResponse({"error": str(e)})


@api_view(['GET'])
@permission_classes([IsAuthenticated])
@csrf_exempt
def inventory_alerts(request):
    try:
        shop = get_user_shop(request.user)
        if not shop:
            return JsonResponse({"error": "User not linked to any shop"}, status=400)
        
        tiles = Tile.objects.filter(shop = shop)

        data = []
        for tile in tiles:
            if tile.stock_quantity <= 10:
                data.append({
                    "tile_name_number": tile.tile_name_number,
                    "tile_type": tile.tile_type,
                    "tile_type2": tile.tile_type2,
                    "stock_quantity": tile.stock_quantity
                })
        return JsonResponse({"inventory_alerts": data})

    except Exception as e:
        return JsonResponse({"error": str(e)})

@api_view(['GET'])
@permission_classes([IsAuthenticated])
@csrf_exempt
def Today(request):
    try:
        shop = get_user_shop(request.user)
        if not shop:
            return JsonResponse({"error": "User not linked to any shop"}, status=400)

        today = timezone.now().date()
        sales = Sale.objects.filter(shop=shop, date=today)

        data = []
        total_amt = 0
        order = 0
        for sale in sales:
            items = SaleItem.objects.filter(sale=sale)
            data.append({
                "customer_name": sale.customer_name,
                "amount": sale.amount,
                "address": sale.address,
                "phone_number": sale.phone_number,
                "items": [{
                    "tile_type": item.tile_type, 
                    "tile_name_number": item.tile_name_number, 
                    "tile_type2": item.tile_type2,
                    "quantity": item.quantity}
                    for item in items]
            })
            total_amt += sale.amount
            order += 1
        return JsonResponse({"today_sales": data, "Revenue": total_amt, "Order": order})

    except Exception as e:
        return JsonResponse({"error": str(e)})


@api_view(['GET'])
@permission_classes([IsAuthenticated])
@csrf_exempt
def sales_comparison(request):
    try:
        shop = get_user_shop(request.user)
        if not shop:
            return JsonResponse({"error": "No shop found"}, status=400)

        Today = date.today()

        current_start = Today.replace(day=1)
        previous_start = current_start - relativedelta(months=1)
        previous_end = current_start - relativedelta(days=1)

        current_sales = Sale.objects.filter(
            shop=shop,
            date__range=[current_start, Today]
        )

        previous_sales = Sale.objects.filter(
            shop=shop,
            date__range=[previous_start, previous_end]
        )

        current_count = current_sales.count()
        previous_count = previous_sales.count()

        growth = 0
        if previous_count > 0:
            growth = ((current_count - previous_count) / previous_count) * 100

        def get_tile_counts(sales):
            tile_map = defaultdict(int)

            for sale in sales:
                items = SaleItem.objects.filter(sale=sale)
                for item in items:
                    key = f"{item.tile_type}_{item.tile_name_number}_{item.tile_type2}"
                    tile_map[key] += item.quantity or 1

            return tile_map

        current_tiles = get_tile_counts(current_sales)
        previous_tiles = get_tile_counts(previous_sales)

        def top_tiles(tile_map):
            return sorted(tile_map.items(), key=lambda x: x[1], reverse=True)[:5]

        top_current = top_tiles(current_tiles)
        top_previous = top_tiles(previous_tiles)

        trending_up = []
        trending_down = []

        all_tiles = set(current_tiles.keys()).union(set(previous_tiles.keys()))

        for tile in all_tiles:
            curr = current_tiles.get(tile, 0)
            prev = previous_tiles.get(tile, 0)

            if curr > prev:
                trending_up.append({
                    "tile": tile,
                    "increase": curr - prev
                })
            elif prev > curr:
                trending_down.append({
                    "tile": tile,
                    "decrease": prev - curr
                })

        return JsonResponse({
            "current_month_sales": current_count,
            "previous_month_sales": previous_count,
            "growth_percentage": round(growth, 2),
            "top_tiles_current": top_current,
            "top_tiles_previous": top_previous,
            "trending_up": trending_up[:5],
            "trending_down": trending_down[:5]
        })

    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)