from django.forms import ModelForm
from .models import Order


class OrderForm(ModelForm):
    class Meta:
        model = Order      #model name from where we have to take the fields
        fields = '__all__'   #select all the fields from 'Order' Model.

