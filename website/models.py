from django.contrib.auth.models import User
from django.db import models

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
    product_type_name = models.CharField(max_length=255, null=True)

    def __str__(self):
        return self.product_type_name


class Product(models.Model):
    seller = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )
    product_type = models.ForeignKey(ProductType)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=8, decimal_places=2, null=False)
    quantity = models.IntegerField()








