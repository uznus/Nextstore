from django.contrib import admin

from .models import *


admin.site.register(User)
admin.site.register(Order)
admin.site.register(FavouriteProduct)
admin.site.register(FeedBack)