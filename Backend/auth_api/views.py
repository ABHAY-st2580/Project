from django.contrib.auth.models import User
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Shop, Membership

@api_view(['POST'])
def register(request):
    fname = request.data.get("fname")
    lname = request.data.get("lname")
    username = request.data.get("username")
    password = request.data.get("password")
    shop_name = request.data.get("shop_name")
    shop_location = request.data.get("shop_location", "Not specified")
    role = request.data.get("role", "OWNER")
    if not all([username, password, shop_name]):
        return Response({"error": "All fields required"}, status=400)

    if User.objects.filter(username=username).exists():
        return Response({"error": "User already exists"}, status=400)

    user = User.objects.create_user(username=username, password=password, first_name=fname, last_name=lname)

    shop = Shop.objects.create(shop_name=shop_name, location=shop_location)

    Membership.objects.create(
        user=user,
        shop=shop,
        role=role
    )

    return Response({"message": "User + Shop created"})

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_all_shops(request):
    shops = Shop.objects.all()
    data = [{"shop_name": shop.shop_name, "location": shop.location} for shop in shops]
    return Response(data)