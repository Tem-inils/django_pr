from django.contrib import admin
from .models import User, Product, UserCart, Restaurant

admin.site.register(User)
admin.site.register(Product)
admin.site.register(UserCart)
admin.site.register(Restaurant)
