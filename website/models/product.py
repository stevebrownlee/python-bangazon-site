from django.contrib.auth.models import User
from django.db import models
from .product_type import ProductType


class Product(models.Model):
    seller = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True, blank=True
    )
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    price = models.IntegerField()
    quantity = models.IntegerField()
    product_type = models.ForeignKey(
        ProductType,
        on_delete=models.DO_NOTHING
    )
