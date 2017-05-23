from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.template import RequestContext
from website.forms import ProductForm
from website.forms import UserForm, Product



def product_detail(request, product_id):
    """
    purpose: gets a single product to be viewed on product/product_detail.html
    author: James Tonkin
    args: request allows Django to see user session data
          product_id is used to generate the individual product
    returns: Combines product_detail.html with product dictionary and returns the request with that rendered text.
    """

    product = Product.objects.get(pk=product_id)
    template_name = 'product/product_detail.html'
    return render(request, template_name, {'product': product})
