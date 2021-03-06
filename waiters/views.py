from django.shortcuts import render, render_to_response
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth.views import logout
from django.contrib.auth.models import User
from .forms import CreateOrderForm
from .models import waiterprofile, Order
from django.contrib import auth
from django.template.context_processors import csrf
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
# def create_order(request):
#     return render(request, 'create_order.html', {})

@login_required
def waiter_abilities(request):
    def get_queryset(self):
        queryset = User.objects.filter(profession='w')
        return queryset
    return render(request, 'abilities.html', {})

@login_required
def logout_view(request):
    def get_queryset(self):
        queryset = User.objects.filter(profession='w')
        return queryset
    logout(request)
    return HttpResponseRedirect('http://127.0.0.1:8000')

@login_required
def createorder(request):
    def get_queryset(self):
        queryset = User.objects.filter(profession='w')
        return queryset
    # queryset = waiterprofile.objects.filter(id=self.request.id)
    if request.method != 'POST':
        form = CreateOrderForm()
    else:
        form = CreateOrderForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('http://127.0.0.1:8000/waiter/orders/')

    context = {'form': form}
    return render(request, 'create_order.html', context)

@login_required
def orders_view(request):
    def get_queryset(self):
        queryset = User.objects.filter(profession='w')
        return queryset
    # permission_classes = (IsAuthenticated,)
    orders = Order.objects.filter(waiter_id=request.user)
    context = {'orders': orders}
    return render(request, 'w_orders.html', context)

@login_required
def order_view(request, order_id):
    def get_queryset(self):
        queryset = User.objects.filter(profession='w')
        return queryset
    order = Order.objects.get(id=order_id)
    context = {'order': order}
    return render(request, 'order.html', context)

@login_required
def edit_order(request, order_id):
    def get_queryset(self):
        queryset = User.objects.filter(profession='w')
        return queryset
    order = Order.objects.get(id=order_id)
    if request.method != 'POST':
        form = CreateOrderForm(instance=order)
    else:
        form = form = CreateOrderForm(instance=order, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('http://127.0.0.1:8000/manager/wlist/{order_id}'.format(order_id=order_id))

    context = {'Order': order, 'form': form}
    return render(request, 'edit_order.html', context)

# def login(request):
#     #print('WE ARE HERE')
#     if request.method == 'POST':
#         form = LoginForm(request.POST)
#         if form.is_valid():
#             first_name = form.cleaned_data['first_name']
#             last_name = form.cleaned_data['last_name']
#             password = form.cleaned_data['password']
#             authenticated_user = authenticate(first_name=request.POST['first_name'],
#                                               last_name=request.POST['last_name'], password=request.POST['password'])
#             return HttpResponseRedirect('http://127.0.0.1:8000/waiter')
#     else:
#         form = LoginForm()
#     return render(request, 'w_login.html', {'form': form})

# def login(request):
#     context = {}
#     context.update(csrf(request))
#     if request.method == 'POST':
#         first_name = request.POST.get('first_name', '')
#         last_name = request.POST.get('last_name', '')
#         password = request.POST.get('password', '')
#         user = auth.authenticate(first_name=first_name, last_name=last_name, password=password)
#         if user is not None:
#             auth.login(request, user)
#             return HttpResponseRedirect('http://127.0.0.1:8000/waiter')
#         else:
#             context['login_error'] = 'Пользователь не найден'
#             return render_to_response('w_login.html', context)
#     else:
#         return render_to_response('w_login.html', context)


