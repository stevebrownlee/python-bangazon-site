from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.template import RequestContext

from website.forms import ProductForm
from website.forms import UserForm
from website.models import Product, Order, LineItem


def shopping_cart(request): 
        user = request.user
        user_order = Order.objects.get_or_create(payment_type_id = None, user_id = user.id)
        template_name = 'shopping_cart.html'
        return render(request, template_name, {'open_order': user_order[0].id})
       
        products_on_order = LineItem.objects.filter(order_id = user_order[0].id)
        return render(request, template_name, {'products_on_order': products_on_order})
