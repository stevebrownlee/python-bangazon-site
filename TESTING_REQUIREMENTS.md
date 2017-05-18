[Testing basics](https://docs.djangoproject.com/en/1.11/intro/tutorial05/#the-django-test-client) 
[Testing examples](https://docs.djangoproject.com/en/1.11/intro/tutorial05/)

* Verify that when a specific product category view (e.g. Electronics) is requested, that there are products in the response context
* Verify that when n products are added to an order that the Order Summary view has those products in the response context
* Verify that when a product is created that the Product Detail view has the correct product in the response context
* Verify that when a product is created that the Product Detail view has the title, description, price and quantity are in the response body
* Verify that the Order History view for a customer has all of the orders in the request context
* Verify that the Payment Types view for a customer has all of the payment types in the request context