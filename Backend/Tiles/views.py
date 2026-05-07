from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Tile
import json

@csrf_exempt
def add_tile_design(request):
    if request.method != 'POST':
        return JsonResponse({"error": "Only POST allowed"}, status=405)
    try:
        data = json.loads(request.body)

        tile_type = data.get("tile_type")
        tile_type2 = data.get("tile_type2")
        tile_name_number = data.get("tile_name_number")
        price_per_box = data.get("price_per_box")
        stock_quantity = data.get("stock_quantity")

        if not all([tile_type, tile_type2, tile_name_number, price_per_box, stock_quantity]):
            return JsonResponse({"error": "All fields required"}, status=400)

        if Tile.objects.filter(
            tile_type=tile_type,
            tile_type2=tile_type2,
            tile_name_number=tile_name_number
        ).exists():
            return JsonResponse({"error": "Tile already exists"}, status=400)

        tile = Tile.objects.create(
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

@csrf_exempt
def get_tile_design(request):
  if request.method == 'GET':
    try:
      tiles = Tile.objects.all()
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
      data = json.loads(request.body)

      tile_name_number = data.get("tile_name_number")
      tile_type = data.get("tile_type")
      tile_type2 = data.get("tile_type2")

      if not all([tile_type, tile_type2, tile_name_number]):
            return JsonResponse({
                "error": "All fields are required"
            }, status=400)

      tile = Tile.objects.filter(
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




