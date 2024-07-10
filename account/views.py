from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework import status
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from rest_framework.permissions import IsAuthenticated

from .models import *
from .serializers import *


@api_view(['POST'])
def signin(request):
    username = request.data.get('username')
    password = request.data.get('password')
    user = authenticate(username=username, password=password)
    print(username)
    if user is not None:
        token = Token.objects.get_or_create(user=user)[0]
        return Response({'token': token.key})
    else:
        return Response('Invalid credentials')


@api_view(['POST'])
def user_create(request):
    first_name = request.data.get('first_name')
    last_name = request.data.get("last_name")
    phone = request.data.get('phone')
    email = request.data.get('email')
    icon = request.data.get('icon')
    username = request.data.get('username')
    password = request.data.get('password')
    user = User.objects.create_user(
        first_name=first_name,
        last_name=last_name,
        phone=phone,
        email=email,
        icon=icon,
        username=username,
        password=password
    )
    token = Token.objects.get_or_create(user=user)
    return Response({'ok': True, 'token': token[0].key}, status=200)


@api_view(['GET', 'POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def account_managament(request):
    user = request.user
    if request.method == 'GET':
        serializer = UserSerializer(user).data
        return Response(serializer, status=status.HTTP_200_OK)
    if request.method == 'POST':
        full_name = request.data.get('full_name')
        phone = request.data.get('phone')
        bio = request.data.get('bio')
        if full_name:
            full_name = full_name.split(' ')
            user.first_name = full_name[0] 
            user.last_name = full_name[1]
        if phone: user.phone = phone
        if bio: user.bio = bio
        user.save()
        return Response({'Message': 'Informations changed successfully!'}, status=status.HTTP_202_ACCEPTED)
    

@api_view(['GET', "POST"])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def order_product(request, pk):
    user = request.user
    product = Product.objects.get(id=pk)
    quantity = request.data.get('quantity')
    new_order = Order.objects.create(
        user=user,
        product=product,
        quantity=quantity
    )
    serializer = OrderSerializer(instance=new_order).data
    return Response(serializer, status=status.HTTP_200_OK)


@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def get_orders(request):
    user = request.user
    status = request.data.get('status')
    orders = Order.objects.filter(user=user)
    if status:
        orders = Order.objects.filter(user=user, status=status)
        serializer = OrderSerializer(instance=orders, many=True).data
        return Response(serializer, status=200)
    else:
        serializer = OrderSerializer(instance=orders, many=True).data
        return Response(serializer, status=200)