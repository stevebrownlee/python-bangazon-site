from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.template import RequestContext
from website.forms import ProductForm
from website.forms import UserForm
from website.models import Product



def product_detail(request, product_id):
    """

    author: James Tonkin
    """

    product = get_object_or_404(models.Product, pk=product_id)
    return render(request, 'product_detail.html', {'product': product})
