from django.conf.urls import url

from . import views

app_name = "website"
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^login$', views.login_user, name='login'),
    url(r'^logout$', views.user_logout, name='logout'),
    url(r'^register$', views.register, name='register'),
    url(r'^products', views.list_products, name='products'),
    url(r'^sell$', views.sell_product, name='sell'),
    url(r'^product/(?P<id>\d+)/$', views.detail_product, name='detail'),
    url(r'^(?P<id>\d+)/edit', views.edit_product, name='edit'),
    url(r'^(?P<id>\d+)/delete', views.delete_product, name='delete'),
]
