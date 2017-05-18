"""
djangazon model configuration for payment type
"""

from django.db import models


class PaymentType(models.Model):
    """
    This class models a payment type in the database. 

    ----Fields---- 
    account_number(decimal): account number

    Author: ?  
    """
    
    account_number = models.DecimalField(max_digits=20, decimal_places=0)
