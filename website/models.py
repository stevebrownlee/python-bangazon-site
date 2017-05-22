from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Profile(User):
    """
    purpose: Creates Category table within database
        Example useage: 

    author: Taylor Perkins, Justin Short

    args: models.Model: (NA): models class given by Django

    returns: (None): N/A
    """      
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):  # __unicode__ on Python 2
        return self.user.first_name




class Category(models.Model):
    """
    purpose: Creates Category table within database
        Example useage: 

    author: Taylor Perkins, Justin Short

    args: models.Model: (NA): models class given by Django

    returns: (None): N/A
    """      
    category_name = models.TextField()    

    def __str__(self):  # __unicode__ on Python 2
        return self.category_name

class Product(models.Model):
    """
    purpose: Creates Product table within database
        Example useage: 

    author: Taylor Perkins, Justin Short, Casey Dailey

    args: models.Model: (NA): models class given by Django

    returns: (None): N/A
    """      
    seller = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )
    #django will display a dropdown with these choices
    CATEGORY_CHOICES = (
    ('electronics','ELECTRONICS'),
    ('sports', 'SPORTS'),
    ('home','HOME'),
    ('general','GENERAL'),
    ('clothing','CLOTHING'),
    )
    product_category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        choices=CATEGORY_CHOICES
    )
    quantity = models.IntegerField(null=False)
    description = models.TextField(null=False, max_length=500)
    price = models.DecimalField(max_digits=5, decimal_places=2, null=False)
    date_created = models.DateField(auto_now=True, auto_now_add=False)  # This auto generates date on creation
    title = models.CharField(max_length=255)

    def __str__(self):  # __unicode__ on Python 2
        return self.title


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
    account_number = models.IntegerField(range(12, 20))

    def __str__(self):  # __unicode__ on Python 2
        return self.name


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
    payment_type = models.ForeignKey(
        PaymentType,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )   
    date_complete = models.DateField(null=True, blank=True, auto_now=False, auto_now_add=False)  # This will get filled upon order completion



