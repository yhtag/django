from django.forms import ModelForm
from accounts.models import *
class OrderForm(ModelForm):
    class Meta:
        model=Order
        fields='__all__'