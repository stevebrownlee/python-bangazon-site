from django.core.urlresolvers import reverse
from django.test import TestCase
from django.utils import timezone

# Verify that the Payment Types view for a customer has all of the payment types in the request context
class PaymentTypeTest(TestCase):
	def test_list_payment_types:
		response = self.client.get(reverse('courses:list'))

	

