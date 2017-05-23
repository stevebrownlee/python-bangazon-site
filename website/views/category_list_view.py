from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.template import RequestContext
from website.forms import ProductForm
from website.forms import UserForm
from website.models import Product, Category



def category_list(request):
    categories = Category.objects.all()
    template_name = 'product/category_list.html'
    return render(request, template_name, {'categories': categories})


