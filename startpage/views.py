# Create your views here.
from django.shortcuts import render
from django.contrib.auth import authenticate
from django.views import View
from django.contrib.auth.views import login
from .forms import LoginForm, RegisterForm
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.contrib.auth.forms import AuthenticationForm
def welcome(request):
    return render(request, 'welcome.html', {'form': LoginForm()})
# def user_login(request):
#     if request.method == 'POST':
#         form = LoginForm(request.POST)
#         if form.is_valid():
#             cd = form.cleaned_data
#             user = authenticate(username=cd['username'], password=cd['password'],
#                                 profession=cd['profession'])
#             if user is not None:
#                 if user.is_active:
#                     login(request, user)
#                     # if request.user.profession == 'asdsad'
#                     # if cd['profession'] == 'w':
#                     return HttpResponseRedirect('http://127.0.0.1:8000/waiter')
#                     # elif cd['profession'] == 'c':
#                     #     return HttpResponseRedirect('http://127.0.0.1:8000/cook')
#                     # else:
#                     #     return HttpResponseRedirect('http://127.0.0.1:8000/manager')
#                 else:
#                     return HttpResponseRedirect('http://127.0.0.1:8000/')
#             else:
#                 return HttpResponseRedirect('http://127.0.0.1:8000/')
#     else:
#         form = LoginForm()
#     return render(request, 'account/login.html', {'form': form})

# def login(request):
#     print('HELLOOOOOO')
#     if request.method == 'POST':
#         form = LoginForm(request.POST)
#         if form.is_valid():
#             username = form.cleaned_data['username']
#             password = form.cleaned_data['password']
#             profession = form.cleaned_data['profession']
#             print(profession)
#             user = authenticate(username=request.POST['username'],
#                                               password=request.POST['password'],
#                                               profession=request.POST['profession'])
#             print('lol', user)
#             if user is not None and user.is_active:
#                 print('pppppppppppp')
#                 auth.login(request, user)
#             # /profession/{aasdasd}
#             # if request.user.profession == 'asdsad'
#                 if profession == 'w':
#                     return HttpResponseRedirect('http://127.0.0.1:8000/waiter')
#                 elif profession == 'c':
#                     return HttpResponseRedirect('http://127.0.0.1:8000/cook')
#                 else:
#                     return HttpResponseRedirect('http://127.0.0.1:8000/manager')
#             else:
#                 return render(request, 'welcome.html',
#                               {'form': form})
#     else:
#         form = LoginForm()
#     return render(request, 'welcome.html', {'form': form})

def register(request):
    if request.method != 'POST':
        form = RegisterForm
    else:
        form = RegisterForm(data=request.POST)
        if form.is_valid():
            new_user = form.save()
            return HttpResponseRedirect('http://127.0.0.1:8000/')

    context = {'form': form}
    return render(request, 'register.html', context)

# def LoginFormView(FormView):
#     form_class = AuthenticationForm
#     template_name = 'welcome.html'
#     def form_valid(self, form):
#         self.user = form.get_user()
#         login(self.request, self.user)
#         return super(LoginFormView, self).is_valid(form)