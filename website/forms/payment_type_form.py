from django import forms
from website.models.payment_type_model import PaymentType

class PaymentTypeForm(forms.ModelForm):

    class Meta:
        model = PaymentType
        fields = ('account_number',)