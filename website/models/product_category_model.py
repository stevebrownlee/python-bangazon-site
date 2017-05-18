"""
djangazon model configuration for category
"""

from django.db import models


class Category (models.Model):
    """
    This class models a product category in the database.

    ----Fields----
    label(character): a category's title
    ETC . . . 

    Author: ?
    """

    label = models.CharField(max_length=255)
