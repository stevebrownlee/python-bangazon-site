from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.template import RequestContext
from website.forms import ProductForm
from website.forms import UserForm
from website.models import Product



def shopping_cart(request, product_id):
    """
    purpose: get the list of products in current order on a page
    author: Dean Smith
    args: request allows Django to see user session data
          product_id is used to generate the individual product
    returns: Combines product_detail.html with product dictionary and returns the request with that rendered text.
    """
    if request.method == 'POST':
        form_
    products_in_cart = LineItem.objects.get(pk=lineitem)
    li = LineItem(

        )
    template_name = 'product/product_detail.html'
    return render(request, template_name, {'product': product})

def sell_product(request):
    # if request.method == 'GET':
    #     product_form = ProductForm()
    #     template_name = 'product/create.html'
    #     return render(request, template_name, {'product_form': product_form})

    if request.method == 'POST':
        form_data = request.POST
        c = Category.objects.get(pk=form_data['category'])
        p = Product(
            seller = request.user,
            title = form_data['title'],
            description = form_data['description'],
            price = form_data['price'],
            quantity = form_data['quantity'],
            date = 'date',
            category = c,
        )
        p.save()
        template_name = 'product/product_detail.html'
        return render(request, template_name, {'product': form_data})
