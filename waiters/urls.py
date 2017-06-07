from django.conf.urls import url, include
from django.contrib import admin
from .views import createorder, waiter_abilities, logout_view, orders_view
# from django.contrib.auth.views import login

urlpatterns = [
    url(r'^create_order/$', createorder, name='create_order'),
    url(r'^$', waiter_abilities, name='your abilities'),
    url(r'^logout/$', logout_view, name='logout'),
    url(r'^orders/$', orders_view, name='orders'),
]