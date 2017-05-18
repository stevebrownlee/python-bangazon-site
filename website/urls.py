from django.conf.urls import url

from . import views

app_name = "website"
urlpatterns = [
    url(r'^$', views.index_view.index, name='index'),
    url(r'^login$', views.login_user_view.login_user, name='login'),
    url(r'^logout$', views.user_logout_view.user_logout, name='logout'),
    url(r'^register$', views.register_view.register, name='register'),
    url(r'^sell$', views.sell_product_view.sell_product, name='sell'),
    url(r'^products$', views.list_products_view.list_products, name='list_products'),
]