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
        self.user = User.objects.create_user(
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
            seller_id=self.user.pk,
            category_id=product_category.pk,
            price=99.85,
            quantity=1
        )

        self.payment_type = PaymentType.objects.create(
            user=self.user,
            name="Visa",
            account_number=987654321
        )

        self.payment_type_two = PaymentType.objects.create(
            user=self.user,
            name="Mastercard",
            account_number=87567889
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
    def test_payment_type_detail_view_has_all_information(self):
        """
        purpose: test that when a payment type is created, the payment detail view contains the title, description,
        price, and quantity
        author: Helana Nosrat, Dean Smith
        args:
        returns: pass/fail based upon successful/unseccessful assertion
        """
        response = self.client.get(reverse('website:paymentlist', args={self.user.pk}))
        self.assertContains(response, self.payment_type.name)
        self.assertContains(response, self.payment_type.account_number)