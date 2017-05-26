from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import get_object_or_404, render
from django.core.exceptions import ObjectDoesNotExist
from django.template import RequestContext


from website.forms import UserForm, ProductForm, AddPaymentForm
from website.models import Product, Category, PaymentType, Order, UserOrder

def index(request):
    template_name = 'index.html'
    top_20_products =  Product.objects.all().order_by("-id")[:20]
    return render(request, template_name, {'top_20_products':top_20_products})

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
    purpose: produce a form for the user to create a product to sell

    author: casey dailey

    args: request

    returns: redirect to detail view for product created
    """

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

            #create an instance of category of where category_name = the user's choice
            product_category = Category.objects.get(category_name=form_data['product_category'])
        )
        p.save()
        return HttpResponseRedirect('product_details/{}'.format(p.id))

def add_payment_type(request):
    '''
    purpose: Allows user to add a payment type to their account, from a submenu in the acount information view

        For an example, visit /product_details/1/ to see a view on the first product created
        displaying title, description, quantity, price/unit, and "Add to order" button

    author: Harry Epstein

    args: name: (string), acount number of credit card

    returns: (render): a view of of the request, template to use, and product obj
    '''
    if request.method == 'GET':
        add_payment_form = AddPaymentForm()
        template_name = 'account/add_payment.html'
        return render(request, template_name, {'add_payment_form': add_payment_form})

    elif request.method == 'POST':
        form_data = request.POST

        p = PaymentType(
            user = request.user,
            name = form_data['name'],
            account_number = form_data['account_number']
        )
        p.save()
        template_name = 'account/add_payment.html'
        return HttpResponseRedirect('/view_account')
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

        if the user clicks "add to order". Their current open order will be updated and the
        user will be routed to that order.

        For an example, visit /product_details/1/ to see a view on the first product created
        displaying title, description, quantity, price/unit, and "Add to order" button

    author: Taylor Perkins, Justin Short

    args: name(string) account type (credit card company); account_number (integer): 12 digit credit card number

    returns: (render): adds the payment type and account name to the database and returns the view of the account information view (/view_account)

    args: product_id: (integer): id of product we are viewing

    returns: (render): a view of of the request, template to use, and product obj
    """
    if request.method == "GET":
        template_name = 'product/details.html'
        product = get_object_or_404(Product, pk=product_id)
        print(product)

    elif request.method == "POST":
        product = get_object_or_404(Product, pk=product_id)
        template_name = 'product/details.html'
        all_orders = Order.objects.filter(buyer=request.user)

        try:
            open_order = all_orders.get(date_complete__isnull=True)
            print(open_order)
            user_order = UserOrder(
                product=product,
                order=open_order)
            user_order.save()

            return HttpResponseRedirect('/view_order/{}'.format(open_order.id))

        except ObjectDoesNotExist:
            print("DoesNotExistError")
            open_order = Order(
                buyer = request.user,
                payment_type = None,
                date_complete = None)
            open_order.save()
            user_order = UserOrder(
                product=product,
                order=open_order)
            user_order.save()
            users_orders = Order.objects.filter(buyer=request.user)
            print(users_orders)

            return HttpResponseRedirect('/view_order/{}'.format(open_order.id))

    return render(request, template_name, {
        "product": product})


def view_specific_product(request, category_id):
    """
    purpose: Allows user to view a specific category view, which contains all products directly related to the given category

        For an example, visit /product_category/1 to see a view on the first category created
        dispaying all products related. All products also have links sending you directly to their specific page

    author: Taylor Perkins

    args: category_id: (integer): id of category we are viewing

    returns: (render): a view of of the request, template to use, and product obj
                (category): category we are viewing
                (products): all products related to given category
    """
    template_name = 'product/category.html'
    category = get_object_or_404(Category, pk=category_id)
    products = Product.objects.filter(product_category=category)
    print(products)
    return render(request, template_name, {
        "category": category,
        "products": products})

def view_account(request):
    template_name = 'account/view_account.html'
    return render(request, template_name)

def edit_account(request):
    template_name = 'account/edit_account.html'
    return render(request, template_name)

# @login_required
def edit_payment_type(request):
    payment_types = PaymentType.objects.filter(user=request.user)
    template_name = 'account/edit_payment.html'
    if request.method == "POST":
        payment_type = PaymentType.objects.get(pk=request.POST.get('payment_type'))
        payment_type.delete()
    return render(request, template_name, {
        "payment_types": payment_types
        })

@login_required
def view_order(request, order_id):
    """
    purpose: present user order and handle interaction with cart
    author: casey dailey
    args: request, order_id
    returns:
    """
    user_order = UserOrder.objects.filter(order=Order.objects.get(pk=order_id))
    print(user_order)
    template_name = 'orders/view_order.html'

    if request.method == 'GET':
        print('fullstack')
        return render(request, template_name, {
            "products": user_order})

    elif 'delete' in request.POST:
        print(request.POST.get("product"))
        product1 = UserOrder.objects.get(pk=request.POST.get("product"))
        print("This is your product{}".format(product1))
        product1.delete()
        return HttpResponseRedirect('/view_order/{}'.format(order_id))

    elif 'checkout' in request.POST:
        return HttpResponseRedirect('/view_checkout/{}'.format(order_id))

    elif 'cancel_order' in request.POST:
        order = Order.objects.get(pk=order_id)
        order.delete()
        return HttpResponseRedirect('/')

    # return render(request, template_name, {
    #         "products": user_order})

@login_required
def view_checkout(request, order_id):
    if request.method == 'GET':
        products = Product.objects.filter(order=order_id)
        payment_types = PaymentType.objects.filter(user=request.user)
        template_name = 'orders/view_checkout.html'
        return render(request, template_name, {
            "products": products,
            "payment_types": payment_types
            })
    elif request.method == 'POST':
        payment_type = PaymentType.objects.get(pk=request.POST.get('select'))
        user_order = Order.objects.get(pk=order_id)
        user_order.payment_type = payment_type
        user_order.save()
        return HttpResponseRedirect('/order_complete/{}'.format(order_id))

def order_complete(request, order_id):
    if request.method == 'GET':
        template_name = 'orders/order_complete.html'
        return render(request, template_name)
