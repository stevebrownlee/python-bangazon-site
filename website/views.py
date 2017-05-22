from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import get_object_or_404, render
from django.template import RequestContext

from website.forms import UserForm, ProductForm
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
        username=request.POST['username']
        password=request.POST['password']
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

def sell_product(request):
        if request.method == 'GET':
            product_form = ProductForm()
            template_name = 'product/create.html'
            return render(request, template_name, {'product_form': product_form})

        elif request.method == 'POST':
            form_data = request.POST

            p = Product(
                seller = request.user,
                title = form_data['title'],
                description = form_data['description'],
                price = form_data['price'],
                quantity = form_data['quantity'],
            )
            p.save()
            template_name = 'product/details.html'
            return render(request, template_name)

def list_products(request):
    template_name = 'product/list.html'
    return render(request, template_name)

def product_categories(request):
    all_categories = Category.objects.all()
    all_products = Product.objects.all().order_by('-id')
    top_three_per_cat = dict()

    for product in all_products:
        print(product.product_category.id)
        try:
            cat_product = top_three_per_cat[product.product_category.id]
            if len(cat_product) < 3:
                cat_product.add(product)
                print(top_three_per_cat)
        except KeyError:
            top_three_per_cat[product.product_category.id] = set()
            top_three_per_cat[product.product_category.id].add(product)
            print(top_three_per_cat)

    print(top_three_per_cat)
    template_name = 'product/categories.html'
    return render(request, template_name, {'all_categories': all_categories, 'product': all_products, 'top_three_per_cat': top_three_per_cat})

def product_details(request, product_id):
    """
    purpose: Allows user to view product_detail view, which contains a very specific view
        for a singular product

        For an example, visit /product_details/1/ to see a view on the first product created
        displaying title, description, quantity, price/unit, and "Add to order" button

    author: Taylor Perkins

    args: product_id: (integer): id of product we are viewing

    returns: (render): a view of of the request, template to use, and product obj
    """
    template_name = 'product/details.html'
    product = get_object_or_404(Product, pk=product_id)
    return render(request, template_name, {
        "product": product})

def product_category(request):
    template_name = 'product/category.html'
    return render(request, template_name)

def view_account(request):
    template_name = 'account/view_account.html'
    return render(request, template_name)

def edit_account(request):
    template_name = 'account/edit_account.html'
    return render(request, template_name)

def edit_payment_type(request):
    template_name = 'account/edit_payment.html'
    return render(request, template_name)

def add_payment_type(request):
    template_name = 'account/add_payment.html'
    return render(request, template_name)

def view_order(request):
    template_name = 'orders/view_order.html'
    return render(request, template_name)

def view_checkout(request):
    template_name = 'orders/view_checkout.html'
    return render(request, template_name)
