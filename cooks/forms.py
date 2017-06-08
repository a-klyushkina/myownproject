from django import forms
from waiters.models import Order

class TakeOrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['status', 'cook']
        labels = {'status': 'статус', 'cook': 'ваш id'}