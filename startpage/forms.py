from django import forms
from managers.models import UserProfile

class RegisterForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['username', 'first_name', 'last_name', 'password', 'profession']
        labels = {'username': '', 'first_name': 'Имя', 'last_name': 'Фамилия', 'password': 'Пароль','profession': 'Должность'}

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
# форма входа
# class LoginForm(forms.ModelForm):
#     class Meta:
#         model = UserProfile
#         fields = ['username', 'password', 'profession']
#         labels = {'username': 'username', 'password': 'Пароль', 'profession': 'Должность'}