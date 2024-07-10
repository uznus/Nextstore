from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import *
from .serializers import *


@api_view(["GET"])
def main(request):
    engkopsotilgan = Product.objects.filter().order_by('ordered')[:8]
    engkopsotilgan_serializer = ProductSerializer(instance=engkopsotilgan, many=True).data
    mashxurlari = Product.objects.filter().order_by('popular')[:8]
    mashxurlari_serializer = ProductSerializer(instance=mashxurlari, many=True).data
    context = {
        'Eng Kop Sotilgan': engkopsotilgan_serializer,
        'Eng Mashxurlari':mashxurlari_serializer
    }
    return Response(context, status=status.HTTP_200_OK)
    

@api_view(['GET'])
def catalogs(request):
    cataloglar = Catalog.objects.all()
    serializer = CatalogSerializer(instance=cataloglar, many=True).data
    return Response(serializer, status=status.HTTP_200_OK)
    

@api_view(['GET'])
def category_get(request, pk):
    categories = Category.objects.filter(catalog_id=pk)
    serializer = CategorySerializer(categories, many=True).data
    return Response(serializer, status=status.HTTP_200_OK)


@api_view(['GET'])
def catalog_view(request):
    category_id = request.data.get('category_id')
    category = Category.objects.get(id=category_id)
    category_serializer = CategorySerializer(instance=category).data
    brands = Brand.objects.filter(category_id=category_id)
    brand_serializer = BrandSerializer(instance=brands, many=True).data
    context = {
        'category': category_serializer,
        'brands': brand_serializer
    }
    return Response(context, status=status.HTTP_200_OK)
    

@api_view(['GET'])
def series_filter(request, brand, pk):
    products = Product.objects.filter(brand_id=brand, series_id=pk)
    serializer = ProductSerializer(instance=products, many=True).data
    return Response(serializer, status=status.HTTP_200_OK)


@api_view(['GET'])
def brand_filter(request, pk):
    productlar = Product.objects.filter(brand_id=pk)
    serializer = ProductSerializer(instance=productlar, many=True).data
    return Response(serializer, status=status.HTTP_200_OK)


@api_view(['GET'])
def product_detail(request, pk):
    product = Product.objects.get(id=pk)
    serializer = ProductDetailSerializer(instance=product).data
    return Response(serializer, status=status.HTTP_200_OK)