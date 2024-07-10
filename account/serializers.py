from rest_framework.serializers import ModelSerializer

from .models import *
from main.serializers import ProductDetailSerializer, ProductSerializer


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('icon', 'first_name', 'last_name', 'phone')


class UserDescriptionSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['icon', 'first_name', 'last_name', 'username', 'phone', 'bio', 'email']


class OrderSerializer(ModelSerializer):
    user = UserDescriptionSerializer()
    product = ProductSerializer()

    class Meta:
        model = Order
        fields = ['user', 'product', 'quantity']


class FavouritheProductSerializer(ModelSerializer):
    user = UserSerializer()
    product = ProductSerializer()

    class Meta:
        model = FavouriteProduct
        fields = ['user', 'product']