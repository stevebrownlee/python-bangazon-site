"""
djangazon model configuration for product
"""

from django.contrib.auth.models import User
from django.db import models


class Product (models.Model):
    """
    This class models a product in the database.

    ----Fields----
    title(character): a product's title
    ETC . . . 

    Author: ?
    """
    seller = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    price = models.IntegerField()
    quantity = models.IntegerField()