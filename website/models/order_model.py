"""
djangazon model configuration for order
"""

from django.db import models


class Order (models.Model):
    """
    This class models an order in the database.

    ----Fields----
    order_date(date): an order's date
    ETC . . . 

    Author: ?
    """

    order_date = models.DateField()


