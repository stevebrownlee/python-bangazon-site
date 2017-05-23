from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.template import RequestContext
from website.forms import ProductForm
from website.forms import UserForm
from website.models import Product, Category



def category_list(request):
    """
    purpose: pulls up "category" view listing all product categories
    author: Bri Wyatt 
    args: request allows Django to see user session data
    returns: Uses template from product/category_list.html and pulls model data from the Category and Product class to return the request with a view of that rendered text.
    """
    categories = Category.objects.all()
    template_name = 'product/category_list.html'
    cat_dict = {'categories': categories}
    return render(request, template_name, cat_dict)
