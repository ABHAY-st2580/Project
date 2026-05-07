from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from django.views.decorators.csrf import csrf_exempt
from .models import Tile
from auth_api.models import Membership, Shop
import json

def get_user_role(user):
    membership = Membership.objects.filter(user=user).first()
    return membership.role if membership else None

def get_user_shop(user):
    membership = Membership.objects.filter(user=user).first()
    return membership.shop if membership else None

@api_view(['POST'])
@permission_classes([IsAuthenticated])
@csrf_exempt
def add_tile_design(request):
    if request.method != 'POST':
        return JsonResponse({"error": "Only POST allowed"}, status=405)
    try:
        shop = get_user_shop(request.user)
        role = get_user_role(request.user)
        if role not in ['OWNER', 'STAFF']:
            return JsonResponse({"error": "Permission denied"}, status=403)
        data = json.loads(request.body)

        tile_type = data.get("tile_type")
        tile_type2 = data.get("tile_type2")
        tile_name_number = data.get("tile_name_number")
        price_per_box = data.get("price_per_box")
        stock_quantity = data.get("stock_quantity")

        if not all([tile_type, tile_type2, tile_name_number, price_per_box, stock_quantity]):
            return JsonResponse({"error": "All fields required"}, status=400)

        if Tile.objects.filter(
            shop = shop,
            tile_type=tile_type,
            tile_type2=tile_type2,
            tile_name_number=tile_name_number
        ).exists():
            return JsonResponse({"error": "Tile already exists"}, status=400)

        tile = Tile.objects.create(
            shop = shop,
            tile_name_number=tile_name_number,
            tile_type=tile_type,
            tile_type2=tile_type2,
            price_per_box=price_per_box,
            stock_quantity=stock_quantity
        )

        return JsonResponse({
            "message": "Tile added",
            "tile_id": tile.tile_id
        }, status=201)

    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
@csrf_exempt
def get_tile_design(request):
  if request.method == 'GET':
    try:
      shop = get_user_shop(request.user)
      if not shop:
        return JsonResponse({"error": "User not linked to any shop"}, status=400) 

      tiles = Tile.objects.filter(shop = shop)
      data = []
      for tile in tiles:
        data.append({
          "tile_id": tile.tile_id,
          "tile_type": tile.tile_type,
          "tile_type2": tile.tile_type2,
          "tile_name_number": tile.tile_name_number,
          "price_per_box": tile.price_per_box,
          "stock_quantity": tile.stock_quantity
        })
      return JsonResponse({"tiles": data})
    except Exception as e:
      return JsonResponse({"error": str(e)})
  
  else:
    if request.method == 'POST':
      shop = get_user_shop(request.user)
      role = get_user_role(request.user)
      if role not in ['OWNER', 'STAFF']:
        return JsonResponse({"error": "Permission denied"}, status=403)
      if not shop:
        return JsonResponse({"error": "User not linked to any shop"}, status=400) 
      if not request.body:
        return JsonResponse({"error": "Data is not there"}, status=401) 
      data = json.loads(request.body)
      tile_name_number = data.get("tile_name_number")
      tile_type = data.get("tile_type")
      tile_type2 = data.get("tile_type2")

      if not all([tile_type, tile_type2, tile_name_number]):
            return JsonResponse({
                "error": "All fields are required"
            }, status=400)

      tile = Tile.objects.filter(
            shop = shop,
            tile_type=tile_type,
            tile_type2=tile_type2,
            tile_name_number=tile_name_number
        ).first()

      if not tile:
            return JsonResponse({
                "error": "Tile design not found"
            }, status=404)
      return JsonResponse({
            "tile_id": tile.tile_id,
            "tile_type": tile.tile_type,
            "tile_type2": tile.tile_type2,
            "tile_name_number": tile.tile_name_number,
            "price_per_box": tile.price_per_box,
            "stock_quantity": tile.stock_quantity
        })  




