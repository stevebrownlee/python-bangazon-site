from django.test import Client, TestCase
from django.urls import reverse
from website.models import User, Category, Product


class SpecificCategoryTestCases(TestCase):

    def setUp(self):
        user_one = User.objects.create(username="Test guy", password="test123")        
        self.category_one = Category.objects.create(category_name="electronics")
        self.category_two = Category.objects.create(category_name="home")
        self.category_three = Category.objects.create(category_name="food")

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

        self.product_three = Product.objects.create(
            seller=user_one,
            product_category=self.category_three,
            quantity=2, 
            description="Light Snack", 
            price=350.00, 
            date_created="2014-12-12", 
            title="Goldfish Crackers")

        client = Client()
        client.login(
            username="Test guy",
            password="test123"
        )

    def test_products_exist_in_category_view_response(self):
        """Profile instance exists"""
        response = self.client.get(reverse('website:product_category_view', args={self.category_one.pk}))        
        self.assertContains(response, self.product_one,)
        self.assertEqual(response.context['category'], self.category_one)

    def test_products_do_not_exist_in_category_view_response(self):
        """Profile instance exists"""
        response = self.client.get(reverse('website:product_category_view', args={self.category_one.pk}))        
        self.assertNotContains(response, self.product_two)
        self.assertNotContains(response, self.product_three)
        self.assertEqual(response.context['category'], self.category_one)

