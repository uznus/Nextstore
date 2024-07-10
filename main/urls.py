from django.urls import path

from .views import *


urlpatterns = [
    path('', main),
    path('catalogs/', catalogs),
    path('categories/<int:pk>/', category_get),
    path('catalog/', catalog_view),
    path('brand/<int:pk>/', brand_filter),
    path('series/<int:brand>/<int:pk>/', series_filter),
    path('product_detail/<int:pk>/', product_detail)
]