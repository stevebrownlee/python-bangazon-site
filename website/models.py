import datetime

from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone

# Create your models here.
class Profile(User):
    """
    purpose: Instantiates a customer, and pulls in Django's default user model
    author: Max Baldridge
    args: User: model class given by Django
    returns: (None): N/A
    """      
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):  # __unicode__ on Python 2
        return "This user's name is {}".format(self.user.first_name)



class ProductType(models.Model):
    """
    purpose: Instantiates a product type
    author: Aaron Barfoot
    args: Extends the models.Model Django class
    returns: (None): N/A
    """   
    product_type_name = models.CharField(max_length=255, null=True)

    def __str__(self):
        return self.product_type_name


class Product(models.Model):
    """
    purpose: Instantiates a product
    author: 
    args: Extends the models.Model Django class
    returns: (None): N/A
    """   
    seller = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
    )
    product_type = models.ForeignKey(ProductType)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=8, decimal_places=2, null=False)
    quantity = models.IntegerField(max_length=100)
    # date_added = models.DateTimeField('Date Added')


class Customer(models.Model):
    """
    purpose: Instantiates a customer
    author: Dara Thomas
    args: Extends the models.Model Django class
    returns: (None): N/A
    """   
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    user_name = models.CharField(max_length=30)
    email_address = models.EmailField(max_length=30)
    password = models.CharField(max_length=15)


class PaymentType(models.Model):
    """
    purpose: Instantiates a payment type
    author: Dara Thomas
    args: Extends the models.Model Django class
    returns: (None): N/A
    """   
    payment_type_name = models.CharField(max_length=15)
    account_number = models.IntegerField(max_length=25)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    


class Order(models.Model):
    """
    purpose: Instantiates an order
    author: Dara Thomas
    args: Extends the models.Model Django class
    returns: (None): N/A
    """   
    order_date = models.DateTimeField('Order Date')
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    payment_type = models.ForeignKey(PaymentType, on_delete=models.PROTECT)
    products = models.ManyToManyField(Product, through="ProductOrder")

    # def __str__(self):
    #     return self.order_date



class ProductOrder(models.Model):
    """
    purpose: Instantiates an instance of a product on an order
    author: Dara Thomas
    args: Extends the models.Model Django class
    returns: (None): N/A
    """   
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)





