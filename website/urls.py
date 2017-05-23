from django.conf.urls import url
from website.views.views import *
from website.views.product_details_view import *
from website.views.category_list_view import *

app_name = "website"
urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^login$', login_user, name='login'),
    url(r'^logout$', user_logout, name='logout'),
    url(r'^register$', register, name='register'),
    url(r'^sell$', sell_product, name='sell'),
    url(r'^products$', list_products, name='list_products'),
    url(r'^categories$', category_list, name='category_list'),
    # url(r'^product_detail$', product_detail, name='product_detail'),
    #url(r'^product_detail$', product_detail, name='product_detail'),
    url(r'^product_detail/(?P<product_id>.+?)/$', product_detail, name='product_detail'),
]
