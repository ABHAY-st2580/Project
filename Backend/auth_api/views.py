from django.contrib.auth.models import User
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.http import JsonResponse
from .models import Shop, Membership
from django.views.decorators.csrf import csrf_exempt

@api_view(['POST'])
@csrf_exempt
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


def get_user_shop(user):
    membership = Membership.objects.filter(user=user).first()
    return membership.shop if membership else None

def get_user_role(user):
    membership = Membership.objects.filter(user=user).first()
    return membership.role if membership else None


@api_view(['GET'])
@permission_classes([IsAuthenticated])
@csrf_exempt
def get_profile(request):
    try:
        user = request.user
        shop = get_user_shop(user)
        role = get_user_role(user)


        data = {
            "username": user.username,
            "fname": user.first_name,
            "lname": user.last_name,
            "phone_number": getattr(user, "phone_number", ""),  # safe access
            "role": role,

            "shop_name": shop.shop_name if shop else "",
            "shop_address": getattr(shop, "shop_location", ""),
        }

        return JsonResponse(data, status=200)

    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)