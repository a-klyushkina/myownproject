from django.shortcuts import render
from waiters.models import Order
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import TakeOrderForm
@login_required
def cook_abilities(request):
    def get_queryset(self):
        queryset = User.objects.filter(profession='c')
        return queryset
    return render(request, 'c_abilities.html', {})

@login_required
def orders(request):
    def get_queryset(self):
        queryset = User.objects.filter(profession='c')
        return queryset
    orders = Order.objects.filter(status='Принят')
    context = {'orders': orders}
    return render(request, 'c_orders.html', context)

@login_required
def your_orders(request):
    def get_queryset(self):
        queryset = User.objects.filter(profession='c')
        return queryset
    orders = Order.objects.filter(cook=request.user)
    context = context = {'orders': orders}
    return render(request, 'your_orders.html', context)

@login_required
def logout_view(request):
    def get_queryset(self):
        queryset = User.objects.filter(profession='c')
        return queryset
    logout(request)
    return HttpResponseRedirect('http://127.0.0.1:8000')

@login_required
def order_view(request, order_id):
    def get_queryset(self):
        queryset = User.objects.filter(profession='m')
        return queryset
    order = Order.objects.get(id=order_id)
    context = {'order': order}
    return render(request, 'orderview.html', context)

