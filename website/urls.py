from django.conf.urls import url

from . import views

app_name = "website"
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^register$', views.register, name='register'),
    url(r'^login$', views.login_user, name='login'),
    url(r'^logout$', views.user_logout, name='logout'),
    url(r'^sell_product$', views.sell_product, name='sell'),
    url(r'^product_category$', views.product_category, name='productCategoryView'),
    url(r'^product_categories$', views.product_categories, name='productCategoriesView'),
    url(r'^product_details$', views.product_details, name='productDetails'),
    url(r'^view_account$', views.view_account, name='viewAccount'),
    url(r'^edit_user_account$', views.edit_account, name='editAccount'),
    url(r'^edit_payment_type$', views.edit_payment_type, name='editPaymentType'),
    url(r'^add_payment_type$', views.add_payment_type, name='addPaymentType'),    
    url(r'^view_order$', views.view_order, name='viewOrder'),
    url(r'^view_checkout$', views.view_checkout, name='viewCheckout'),
]
