from django.conf.urls import url, include
from django.contrib import admin
from .views import cook_abilities, orders, logout_view
from django.contrib.auth.views import login

urlpatterns = [
    url(r'^$', cook_abilities, name='abilities'),
    url(r'^orders', orders, name='orders'),
    url(r'^login/$', login, {'template_name': 'c_login.html'}, name='login'),
    url(r'logout/$', logout_view, name='logout')

]