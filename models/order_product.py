from django.db import models
from .product import Product
from .order import Order


class OrderProduct(models.Model):
    order = models.ForeignKey(
      Order,
      on_delete=models.DO_NOTHING,
      related_name='line_items',
    )
    product = models.ForeignKey(
      Product,
      on_delete=models.DO_NOTHING,
      related_name='line_items',
    )
