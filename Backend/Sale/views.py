from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Sale, SaleItem
import json


@csrf_exempt
def add_sale(request):
  if request.method == "POST":
    try:
      try:
        data = json.loads(request.body)
        cust_name = data.get("customer_name")
        amt = data.get("amount")
        rem_amt = data.get("remaining_amount")
        address = data.get("address")
        phone = data.get("phone_number")
      except json.JSONDecodeError:
        return JsonResponse({"error": "Invalid JSON data"})

      sale = Sale.objects.create(
        customer_name = cust_name,
        amount = amt,
        remaining_amount = rem_amt,
        address = address,
        phone_number = phone
      )

      items = data.get("items", [])

      for item in items:
        SaleItem.objects.create(
            sale = sale,
            tile_type = item.get("tile_type"),
            tile_name_number = item.get("tile_name_number"),
            tile_type2 = item.get("tile_type2"),
            quantity = item.get("quantity")
        )
      return JsonResponse({"message": "Sale added successfully", "sale_id": sale.sale_id})
    except Exception as e:
      return JsonResponse({"error": str(e)})
  else:
    return JsonResponse({"error": "Not a post request"})