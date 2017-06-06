from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render, get_object_or_404, redirect
from django.template import RequestContext

from website.forms import UserForm, ProductForm, CategoryForm
from website.models import Product, Category


def index(request):
    template_name = 'index.html'
    return render(request, template_name, {})


# Create your views here.
def register(request):
    '''Handles the creation of a new user for authentication

    Method arguments:
      request -- The full HTTP request object
    '''

    # A boolean value for telling the template whether the registration was successful.
    # Set to False initially. Code changes value to True when registration succeeds.
    registered = False

    # Create a new user by invoking the `create_user` helper method
    # on Django's built-in User model
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)

        if user_form.is_valid():
            # Save the user's form data to the database.
            user = user_form.save()

            # Now we hash the password with the set_password method.
            # Once hashed, we can update the user object.
            user.set_password(user.password)
            user.save()

            # Update our variable to tell the template registration was successful.
            registered = True

        return login_user(request)

    elif request.method == 'GET':
        user_form = UserForm()
        template_name = 'register.html'
        return render(request, template_name, {'user_form': user_form})


def login_user(request):
    '''Handles the creation of a new user for authentication

    Method arguments:
      request -- The full HTTP request object
    '''

    # Obtain the context for the user's request.
    context = RequestContext(request)

    # If the request is a HTTP POST, try to pull out the relevant information.
    if request.method == 'POST':

        # Use the built-in authenticate method to verify
        username = request.POST['username']
        password = request.POST['password']
        authenticated_user = authenticate(username=username, password=password)

        # If authentication was successful, log the user in
        if authenticated_user is not None:
            login(request=request, user=authenticated_user)
            return HttpResponseRedirect('/')

        else:
            # Bad login details were provided. So we can't log the user in.
            print("Invalid login details: {}, {}".format(username, password))
            return HttpResponse("Invalid login details supplied.")

    return render(request, 'login.html', {}, context)


# Use the login_required() decorator to ensure only those logged in can access the view.
@login_required
def user_logout(request):
    # Since we know the user is logged in, we can now just log them out.
    logout(request)

    # Take the user back to the homepage. Is there a way to not hard code
    # in the URL in redirects?????
    return HttpResponseRedirect('/')


def list_products(request):
    """pass"""
    all_products = Product.objects.all()
    context = {
        "title": "Products List",
        "products": all_products
    }

    return render(request, 'product/list.html', context)


def sell_product(request):
    """pass"""
    form = ProductForm(request.POST or None)

    if form.is_valid():
        new_product = form.save(commit=False)
        new_product.seller = request.user
        new_product.save()
        return redirect(new_product.get_absolute_url())

    context = {
        "product_form": form
    }
    return render(request, 'product/create.html', context)


def edit_product(request, id=None):
    """pass"""
    instance = get_object_or_404(Product, id=id)
    form = ProductForm(request.POST or None, instance=instance)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return redirect(instance.get_absolute_url())
    context = {
        "tile": instance.title,
        "instance": instance,
        "product_form": form
    }
    return render(request, 'product/create.html', context)


def detail_product(request, id=None):
    """pass"""
    instance = get_object_or_404(Product, id=id)

    context = {
        "title": "Product Detail",
        "product": instance
    }
    return render(request, 'product/detail.html', context)


def delete_product(request, id=None):
    """pass"""
    instance = get_object_or_404(Product, id=id)
    instance.delete()
    return redirect('website:products')


def add_category(request):
    """pass"""
    form = CategoryForm(request.POST or None)

    if form.is_valid():
        form.save(commit=False)
        form.save()
        return redirect('website:categories')

    context = {
        "category_form": form
    }
    return render(request, 'product/category.html', context)


def list_categories(request):
    """pass"""
    categories = Category.objects.all()
    context = {
        "categories": categories
    }
    return render(request, 'product/category-list.html', context)


def detail_category(request, id=None):
    """pass"""
    instance = get_object_or_404(Category, id=id)

    context = {
        "title": "Category Detail",
        "category": instance
    }
    return render(request, 'product/category-detail.html', context)


def delete_category(request, id=None):
    """pass"""
    instance = get_object_or_404(Category, id=id)
    instance.delete()
    return redirect('website:categories')


def edit_category(request, id=None):
    """pass"""
    instance = get_object_or_404(Category, id=id)
    form = CategoryForm(request.POST or None, instance=instance)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return redirect(instance.get_absolute_url())
    context = {
        "instance": instance,
        "category_form": form
    }
    return render(request, 'product/category.html', context)