"""
djangazon model configuration for the product_order joining table
"""

from django.db import models

from website.models.product_model import Product


class ProductOrder (models.Model):
    """
    This class models the relationship between the Order and Product resources 
    in the database.

    ----Fields----
    product_id(foreign key): Links to Product(ProductID) with a foreign key
    ETC . . . 

    Author: ?
    """

    product_id = models.ForeignKey(Product)