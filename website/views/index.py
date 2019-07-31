from django.shortcuts import render
from website.models import Product

def index(request):
    all_products = Product.objects.all()[:20]
    template_name = 'index.html'
    return render(request, template_name, {"products": all_products})
