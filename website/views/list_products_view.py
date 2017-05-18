from django.shortcuts import render

from website.forms import ProductForm
from website.models.product_model import Product

def list_products(request):
    all_products = Product.objects.all()
    template_name = 'product/list.html'
    return render(request, template_name, {'products': all_products})