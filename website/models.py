from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class User(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    price = models.IntegerField()
    quantity = models.IntegerField()


class Category(models.Model):
    """
    purpose: Creates Category table within database
        Example useage: 

    author: Taylor Perkins, Justin Short

    args: models.Model: (NA): models class given by Django

    returns: (None): N/A
    """      
    category_name = models.TextField(blank=True, null=False, max_length=50)    

class Product(models.Model):
    """
    purpose: Creates Product table within database
        Example useage: 

    author: Taylor Perkins, Justin Short

    args: models.Model: (NA): models class given by Django

    returns: (None): N/A
    """      
    seller = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )
    product_category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
    )
    quantity = models.IntegerField(null=False)
    description = models.TextField(blank=True, null=False, max_length=500)
    price = models.DecimalField(max_digits=5, decimal_places=2, null=False)
    date_created = models.DateField(auto_now=True, auto_now_add=False)  # This auto generates date on creation
    title = models.CharField(max_length=255)


class PaymentType(models.Model):
    """
    purpose: Creates PaymentType table within database
        Example useage: 

    author: Taylor Perkins, Justin Short

    args: models.Model: (NA): models class given by Django

    returns: (None): N/A
    """   
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )   
    name = models.TextField(blank=True, null=False, max_length=50) 
    account_number = models.IntegerField(range(12, 19))


class Order(models.Model):
    """
    purpose: Creates Order table within database
        Example useage: 

    author: Taylor Perkins, Justin Short

    args: models.Model: (NA): models class given by Django

    returns: (None): N/A
    """   
    buyer = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )   
    date_complete = models.DateField(null=True, auto_now=False, auto_now_add=False)  # This will get filled upon order completion











