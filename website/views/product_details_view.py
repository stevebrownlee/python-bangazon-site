from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.template import RequestContext

from website.forms import Product, UserForm, AddToCartForm, LineItem
from website.models import Order



def product_detail(request, product_id):
    """
    purpose: gets a single product to be viewed on product/product_detail.html
    author: James Tonkin
    args: request allows Django to see user session data
          product_id is used to generate the individual product
    returns: Combines product_detail.html with product dictionary and returns
    the request with that rendered text.
    """

    product = Product.objects.get(pk=product_id)
    template_name = 'product/product_detail.html'
    return render(request, template_name, {'product': product})

def get_order(request):
    """
    purpose: Gets user open order or creates a new order.
    author: Helana Nosrat
    args: request allows Django to see user session data
    """
    user = request.user
    user_order = Order.objects.get_or_create(payment_type_id = None, user_id = user.id)
    return user_order
    print("order", user_order)

def add_to_cart(request):
    """
    purpose: Adds products to the order.
    author: Helana Nosrat
    args: request allows Django to see user session data
    returns: returns and renders shopping cart view with products in order.
    """
    if request.method == 'GET':
        add_to_cart_form = AddToCartForm()
        template_name = 'product_detail.html'
        return render(request, template_name, {'add_to_cart_form': add_to_cart_form})

    elif request.method == 'POST':
        order = get_order(request)
        form_data = request.POST
        p = Product.objects.get(pk=form_data['product_id'])
        li = LineItem(
            product=p,
            order=order[0],
        )
        li.save()
        return HttpResponseRedirect('/shopping_cart')
