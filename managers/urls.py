from .views import cprofiles, wprofiles, manager_abilities, cprofile, wprofile, \
    new_waiter, new_cook, edit_cook, edit_waiter, logout_view
from django.conf.urls import url, include
from django.contrib.auth.views import login
urlpatterns = [
    url(r'^$', manager_abilities, name='your abilities'),
    # url(r'^create/$', create_page, name='create'),
    # url(r'^register/$', register, name='register'),
    # url(r'^login/$', login, {'template_name': 'm_login.html'}, name='login'),
    url(r'^logout/$', logout_view , name='logout'),

    url(r'^clist/$', cprofiles, name='list of cooks'), #список поваров
    url(r'^clist/(?P<profile_id>\d+)/$', cprofile, name='cook'), #профиль повара с id
    url(r'^clist/(?P<profile_id>\d+)/edit/', edit_cook, name='edit cook'), #редактирование профиля повара
    url(r'^clist/new_cook/$', new_cook, name='new_cook'), #новый повар

    url(r'^wlist/$', wprofiles, name='list of waiters'), #список официантов
    url(r'^wlist/(?P<profile_id>\d+)/$', wprofile, name='waiter'), #профиль официанта с id
    url(r'^wlist/(?P<profile_id>\d+)/edit/', edit_waiter, name='edit waiter'), #редактирование профиля
    url(r'^wlist/new_waiter/$', new_waiter, name='new_waiter'), #создание нового

]