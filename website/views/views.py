
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render
from django.template import RequestContext

from website.forms import UserForm, ProductForm, PaymentTypeForm
from website.models import Product, Category, PaymentType

def index(request):
    template_name = 'index.html'
    all_products = Product.objects.all().order_by('-id')[:20]
    return render(request, template_name, {'products': all_products})


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

    """
    purpose: add a payment type to the data base
    author: Dean Smith, Helana Nosrat
    args: request allows Django to see user session data
    """

    if request.method == 'GET':
        product_form = ProductForm()
        template_name = 'product/create.html'
        return render(request, template_name, {'product_form': product_form})

    elif request.method == 'POST':
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

def list_products(request):
    all_products = Product.objects.all()
    template_name = 'product/list.html'
    return render(request, template_name, {'products': all_products})

def add_payment_type(request):

    """
    purpose: add a payment type to the data base
    author: Dean Smith, Helana Nosrat
    args: request allows Django to see user session data
    """

    if request.method == 'GET':
        payment_type_form = PaymentTypeForm()
        template_name = 'payment.html'
        return render(request, template_name, {'payment_type_form': payment_type_form})

    elif request.method == 'POST':
        form_data = request.POST
        p = PaymentType(
            user=request.user,
            name=form_data['name'],
            account_number=form_data['account_number'],
        )
        p.save()
        template_name = 'payment.html'
        return render(request, template_name, {'paymenttype': form_data})

def all_payment_types(request):
        user = request.user
        all_payment_types = PaymentType.objects.filter(user_id=user.id)
        template_name = 'list_payment.html'
        payment_type_dict = {'all_payment_types': all_payment_types}
        return render(request, template_name, payment_type_dict)

 