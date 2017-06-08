from django.shortcuts import render
from waiters.models import waiterprofile
from cooks.models import cookprofile
from django.core.urlresolvers import reverse
from .forms import WaiterForm, CookForm
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
# Create your views here.
@login_required
def wprofiles(request):
    def get_queryset(self):
        queryset = User.objects.filter(profession='m')
        return queryset
    profiles = waiterprofile.objects.all()
    context = {'profiles': profiles}

    return render(request, 'waiters_list.html', context)

@login_required
def cprofiles(request):
    def get_queryset(self):
        queryset = User.objects.filter(profession='m')
        return queryset
    profiles = cookprofile.objects.order_by('id')
    context = {'profiles': profiles}
    return render(request, 'cooks_list.html', context)

@login_required
def wprofile(request, profile_id):
    def get_queryset(self):
        queryset = User.objects.filter(profession='m')
        return queryset
    profile = waiterprofile.objects.get(id=profile_id)
    context = {'profile': profile}
    return render(request, 'waiter.html', context)

@login_required
def cprofile(request, profile_id):
    def get_queryset(self):
        queryset = User.objects.filter(profession='m')
        return queryset
    profile = cookprofile.objects.get(id=profile_id)
    context = {'profile': profile}
    return render(request, 'cook.html', context)

@login_required
def manager_abilities(request):
    def get_queryset(self):
        queryset = User.objects.filter(profession='m')
        return queryset
    return render(request, 'manager_abilities.html', {})

@login_required
def create_page(request):
    def get_queryset(self):
        queryset = User.objects.filter(profession='m')
        return queryset
    return render(request, 'create_page.html', {})

@login_required
def new_waiter(request):
    def get_queryset(self):
        queryset = User.objects.filter(profession='m')
        return queryset
    if request.method != 'POST':
        form = WaiterForm
    else:
        form = WaiterForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('http://127.0.0.1:8000/manager/wlist')

    context = {'form': form}
    return render(request, 'new_waiter.html', context)

@login_required
def new_cook(request):
    def get_queryset(self):
        queryset = User.objects.filter(profession='m')
        return queryset
    if request.method != 'POST':
        form = CookForm
    else:
        form = CookForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('http://127.0.0.1:8000/manager/clist')

    context = {'form': form}
    return render(request, 'new_cook.html', context)

@login_required
def edit_waiter(request, profile_id):
    def get_queryset(self):
        queryset = User.objects.filter(profession='m')
        return queryset
    profile = waiterprofile.objects.get(id=profile_id)
    if request.method != 'POST':
        form = WaiterForm(instance=profile)
    else:
        form = WaiterForm(instance=profile, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('http://127.0.0.1:8000/manager/wlist/{profile_id}'.format(profile_id=profile_id))

    context = {'waiterprofile': cookprofile, 'form': form}
    return render(request, 'waiter_edit.html', context)

@login_required
def edit_cook(request, profile_id):
    def get_queryset(self):
        queryset = User.objects.filter(profession='m')
        return queryset
    profile = cookprofile.objects.get(id=profile_id)
    if request.method != 'POST':
        form = CookForm(instance=profile)
    else:
        form = CookForm(instance=profile, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('http://127.0.0.1:8000/manager/clist/{profile_id}'.format(profile_id=profile_id))

    context = {'cookprofile': cookprofile, 'form': form}
    return render(request, 'cook_edit.html', context)

@login_required
def logout_view(request):
    def get_queryset(self):
        queryset = User.objects.filter(profession='m')
        return queryset
    logout(request)
    return HttpResponseRedirect('http://127.0.0.1:8000')



