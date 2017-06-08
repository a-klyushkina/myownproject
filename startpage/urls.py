from django.conf.urls import url, include
from django.contrib import admin
from .views import welcome, register
from django.contrib.auth.views import login
urlpatterns = [
    url(r'^$', login, {'template_name': 'welcome.html'}, name='welcome'),
    url('^register/$', register, name='register'),

]