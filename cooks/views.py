from django.shortcuts import render
from waiters.models import Order
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required

@login_required
def cook_abilities(request):
    return render(request, 'c_abilities.html', {})

@login_required
def orders(request):
    orders = Order.objects.filter(status='Принят')
    context = {'orders': orders}
    return render(request, 'c_orders.html', context)

@login_required
def logout_view(request):
    logout(request)
    return HttpResponseRedirect('http://127.0.0.1:8000')