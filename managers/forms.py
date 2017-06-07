from django import forms
from waiters.models import waiterprofile
from cooks.models import cookprofile
from django.contrib.auth.models import User
from .models import UserProfile

class WaiterForm(forms.ModelForm):
    class Meta:
        model = waiterprofile
        fields = ['name', 'last_name', 'age', 'birth', 'adress', 'phone']
        labels = {'name': 'Имя', 'last_name': 'Фамилия', 'age': 'Возраст', 'birth': 'Дата рождения', 'adress': 'Адрес',
                  'phone': 'Номер телефона'}

class CookForm(forms.ModelForm):
    class Meta:
        model = cookprofile
        fields = ['name', 'last_name', 'age', 'birth', 'adress', 'phone']
        labels = {'name': 'Имя', 'last_name': 'Фамилия', 'age': 'Возраст', 'birth': 'Дата рождения', 'adress': 'Адрес'}
