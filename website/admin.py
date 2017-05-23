from django.contrib import admin
from .models import Category, Product, PaymentType, Order, Profile

# Register your models here.
admin.site.register(Profile)
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(PaymentType)
admin.site.register(Order)

