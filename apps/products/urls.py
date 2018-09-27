from django.conf.urls import url
from . import views

urlpatterns = [
  url(r'^$', views.index, name="index"),
  url(r'^new/$', views.new, name="new"),
  url(r'^create/$', views.create, name="create"),
  url(r'^(?P<product_id>\d+)/add_to_cart/$', views.add_to_cart, name="add_to_cart"),
  url(r'^(?P<product_id>\d+)/remove_from_cart/$', views.remove_from_cart, name="remove_from_cart"),

]