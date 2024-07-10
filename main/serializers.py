from rest_framework.serializers import ModelSerializer

from .models import *


class CatalogSerializer(ModelSerializer):
    class Meta:
        model = Catalog
        fields = ['image', 'name']


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = ('image', 'name', 'total_products')


class ShopSerializer(ModelSerializer):
    class Meta:
        model = Shop
        fields = ['name']


class SeriesSerializer(ModelSerializer):

    class Meta:
        model = Series
        fields = ['name']


class BrandSerializer(ModelSerializer):
    series = SeriesSerializer(many=True)

    class Meta:
        model = Brand
        fields = ['icon', 'name', 'series']


class ColorSerializer(ModelSerializer):
    class Meta:
        model = Color
        fields = ['icon', 'name']


class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = ['image', 'name', 'price', 'ordered']


class ProductDetailSerializer(ModelSerializer):
    color = ColorSerializer()
    shop = ShopSerializer()

    class Meta:
        model = Product
        fields = ['image', 'name', 'color', 'price', 'shop', 'description', 'product_code', 'creatore_code', 'ordered']