from django import forms
from .models import Order, OrderItem

class OrderForm(forms.ModelForm):
    """ Form to Order Product """

    class Meta:
        model = Order
        fields = '__all__'
        exclude = ('payed','user', 'products')
        widgets = {
        'messages':forms.Textarea(attrs={'rows':30,'cols':8}),
        'phone': forms.TextInput(attrs={'pattern': r'[0-9]{2}-[0-9]{3}-[0-9]{4}'})
        }
