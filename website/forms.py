from django.contrib.auth.models import User
from django import forms
from website.models import Product, Category


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'first_name', 'last_name',)


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = ('title', 'description', 'price', 'quantity', 'category')


class CategoryForm(forms.ModelForm):

    class Meta:
        model = Category
        fields = ('name',)
