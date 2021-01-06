from django import forms
from .models import Category,SubCategory,Order

class OrderForm(forms.ModelForm):
    class Meta:
        model= Order
        fields = ('category','sub_category',)
