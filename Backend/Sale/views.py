from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from django.db import transaction
from .models import Sale, SaleItem
from Tiles.models import Tile
from auth_api.models import Shop, Membership
import json

def get_user_shop(user):
    membership = Membership.objects.filter(user=user).first()
    return membership.shop if membership else None

def get_user_role(user):
    membership = Membership.objects.filter(user=user).first()
    return membership.role if membership else None

@api_view(['POST'])
@permission_classes([IsAuthenticated])
@csrf_exempt
def add_sale(request):
    try:
        shop = get_user_shop(request.user)
        role = get_user_role(request.user)
        if role not in ['OWNER', 'STAFF']:
            return JsonResponse({"error": "Permission denied"}, status=403)
        if not shop:
            return Response({"error": "No shop assigned"}, status=400)
        data = json.loads(request.body)

        cust_name = data.get("customer_name")
        amt = data.get("amount")
        rem_amt = data.get("remaining_amount")
        address = data.get("address")
        phone = data.get("phone_number")
        items = data.get("items", [])

        if not items:
            return JsonResponse({"error": "No items provided"}, status=400)

        with transaction.atomic():

            sale = Sale.objects.create(
                shop = shop,
                customer_name=cust_name,
                amount=amt,
                remaining_amount=rem_amt,
                address=address,
                phone_number=phone
            )

            for item in items:
                tile_type = item.get("tile_type")
                tile_name_number = item.get("tile_name_number")
                tile_type2 = item.get("tile_type2")
                qty = item.get("quantity")

                try:
                    tile = Tile.objects.get(
                        shop = shop,
                        tile_type=tile_type,
                        tile_type2=tile_type2,
                        tile_name_number=tile_name_number
                    )
                    if tile.stock_quantity < qty:
                        tile.stock_quantity = 0
                        raise Exception(f"Insufficient stock for {tile_type} {tile_name_number} ({tile_type2}). Available: {tile.stock_quantity}, Requested: {qty}")
                    else:
                        tile.stock_quantity -= qty
                    
                    tile.save()
                except Tile.DoesNotExist:
                    pass

                SaleItem.objects.create(
                    sale=sale,
                    tile_type=tile_type,
                    tile_name_number=tile_name_number,
                    tile_type2=tile_type2,
                    quantity=qty
                )

        return JsonResponse({
            "message": "Sale added successfully",
            "sale_id": sale.sale_id
        }, status=201)

    except Exception as e:
        return JsonResponse({"error": str(e)}, status=400)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
@csrf_exempt
def get_sales(request):
    try:
        shop = get_user_shop(request.user)
        role = get_user_role(request.user)
        if role not in ['OWNER', 'STAFF']:
            return JsonResponse({"error": "Permission denied"}, status=403)
        sales = Sale.objects.filter(shop = shop)
        data = []
        for sale in sales:
            items = SaleItem.objects.filter(sale=sale)[:7]

            item_list = []
            for item in items:
                item_list.append({
                    "tile_type": item.tile_type,
                    "tile_name_number": item.tile_name_number,
                    "HL_L_D_F": item.tile_type2,
                    "quantity": item.quantity
                })

            data.append({
                "sale_id": sale.sale_id,
                "customer_name": sale.customer_name,
                "amount": sale.amount,
                "remaining_amount": sale.remaining_amount,
                "date": str(sale.date),
                "address": sale.address,
                "phone_number": sale.phone_number,
                "items": item_list
            })

        return JsonResponse(data, safe=False)

    except Exception as e:
        return JsonResponse({"error": str(e)})




