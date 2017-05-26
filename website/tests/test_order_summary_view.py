from django.test import Client, TestCase
from django.urls import reverse
from website.models import User, Category, Product, Order, UserOrder


class ProductOrderRelationshipTestCases(TestCase):

    def setUp(self):

        user_one = User.objects.create(username="Test guy", password="test123")


        self.user_order = Order.objects.create(buyer=user_one)

        self.category_one = Category.objects.create(category_name="electronics")
        self.category_two = Category.objects.create(category_name="home")

        self.product_one = Product.objects.create(
            seller=user_one,
            product_category=self.category_one,
            quantity=2,
            description="Something electronic",
            price=350.00,
            date_created="2014-12-12",
            title="Computer")

        self.product_two = Product.objects.create(
            seller=user_one,
            product_category=self.category_two,
            quantity=2,
            description="Comfy",
            price=350.00,
            date_created="2014-12-12",
            title="Chair")

        self.user_order1 = UserOrder.objects.create(product=self.product_one, order=self.user_order)

        self.client = Client()
        self.client.force_login(user_one)


    def test_order_summery_view_has_added_products_in_response(self):
        """order instance exists"""

        print("ellllooooo")
        response = self.client.get(reverse('website:view_order', args={self.user_order.pk}))


        self.assertContains(response, self.user_order1)
