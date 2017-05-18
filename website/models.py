from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Category(models.Model):
    """
    purpose: creates the category table in the database
    author: James Tonkin
    args: models.Model
    returns: N/A
    """
    name = models.CharField(max_length = 255)

    def __str__(self):
        return self.name

class Product(models.Model):
    """
    purpose: creates the product table in the database
    author: James Tonkin
    args: models.Model
    returns: N/A
    """
    category = models.ForeignKey(
        Category,
        on_delete = models.CASCADE,
    )
    seller = models.ForeignKey(
        User,
        on_delete = models.CASCADE,
    )
    title = models.CharField(max_length = 255)
    price = models.IntegerField()
    description = models.TextField(blank = True, null = True)
    quantity = models.IntegerField()
    city = models.CharField(max_length = 255)
    date = models.DateTimeField(auto_now_add=True, blank=True)

class PaymentType(models.Model):
    """
    purpose: creates the payment type table in the database
    author: James Tonkin
    args: models.Model
    returns: N/A
    """
    user = models.ForeignKey(
        User,
        on_delete = models.CASCADE,
    )
    name = models.CharField(max_length = 255)
    account_number = models.IntegerField()

class Order(models.Model):
    """
    purpose: creates the order table in the database
    author: James Tonkin
    args: models.Model
    returns: N/A
    """
    user = models.ForeignKey(
        User,
        on_delete = models.CASCADE,
    )
    payment_type_id = models.IntegerField()

class LineItem(models.Model):
    """
    purpose: creates the lineitem table in the database
    author: James Tonkin
    args: models.Model
    returns: N/A
    """
    order = models.ForeignKey(
        User,
        on_delete = models.CASCADE,
    )
    product = models.ForeignKey(Product)
