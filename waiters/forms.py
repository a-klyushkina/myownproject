from django import forms
from .models import Order

#форма заказа
class CreateOrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['table', 'text', 'remark', 'status', 'waiter']
        labels = {'table': 'Номер столика', 'text': 'заказ', 'remark': 'дополнительно', 'status': 'стадия реализации', 'waiter': 'укажите ваш id'}


