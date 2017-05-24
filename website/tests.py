from django.test import Client, TestCase
from django.urls import reverse
from website.models import *


class ViewsTestCases(TestCase):

    @classmethod
    def setUp(self):
        """
        purpose: create a user, product category, and product for testing
        author: Kayla Brewer
        args: (integer) product_id
        returns: user, category, product objects
        """
        user = User.objects.create_user(
            first_name="Deanward",
            last_name="Smitherton",
            username="sillywabbitz",
            email="deanward@coolbeansalad.com",
            password="1234asdf"
        )

        product_category = Category.objects.create(
            name="Test"
        )

        self.product = Product.objects.create(
            title="Doge",
            description="Grown up pupper. Much smart. Very fluff.",
            seller_id=user.pk,
            category_id=product_category.pk,
            price=99.85,
            quantity=1
        )

        payment_type = PaymentType.objects.create(
            user=user,
            name="Visa",
            account_number=987654321
        )

        client = Client()

        client.login(
            username="sillywabbit",
            password="1234asdf"
        )

    def test_product_detail_view_returns_correct_product(self):
        """
        purpose: test that the when a product is created, the product detail view has the correct product
        in response
        author: Kayla Brewer
        args: (integer) product_id
        returns: pass/fail based upon successful/unsuccessful assertion
        """

        response = self.client.get(reverse('website:product_detail', args={self.product.pk}))
        self.assertEqual(response.context['product'].pk, self.product.pk)

    def test_product_detail_view_has_all_information(self):
        """
        purpose: test that the when a product is created, the product detail view contains the title, description,
        price, and quantity
        author: Kayla Brewer
        args: (integer) product_id
        returns: pass/fail based upon successful/unsuccessful assertion
        """
        response = self.client.get(reverse('website:product_detail', args={self.product.pk}))
        self.assertContains(response, self.product.title)
        self.assertContains(response, self.product.description)
        self.assertContains(response, self.product.price)
        self.assertContains(response, self.product.quantity)

# Verify that the Payment Types view for a customer has all of the payment types in the request context
class PaymentTypeTest(TestCase):
    def test_list_payment_types:
        response = self.client.get(reverse('courses:list'))
