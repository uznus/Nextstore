from django.urls import path

from .views import *


urlpatterns = [
    path('sign-in/', signin),
    path('sign-up/', user_create),
    path('account-managament/', account_managament),
    path('order-product/<int:pk>/', order_product),
    path("my-orders/", get_orders)
]