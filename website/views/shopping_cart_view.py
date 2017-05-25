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
    user_order = Order.objects.filter(user_id = user.id
        ).filter(payment_type_id = None)
    template_name = 'shopping_cart.html'
    if user_order:
        return render(request, template_name, {'open_order': user_order})
    else:
        request.POST
        user_order = Order(
            user = request.user,
        )
        user_order.save()
        return render(request, template_name, {'open_order': user_order.id})

    products_on_order = LineItem.objects.filter(order_id = user_order.id)
    return render(request, template_name, {'products_on_order': products_on_order})
