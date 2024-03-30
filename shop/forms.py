from django import forms

from shop.models import Product, Category


class CreateProductForm(forms.ModelForm):
    # name = forms.CharField(label='Name')
    # description = forms.CharField(label='Description')
    # category = forms.CharField(label='Category')
    # price = forms.CharField(label='Price')

    class Meta:
        model = Product
        fields = ['name', 'description', 'category', 'price']

from django import forms
from shop.models import SavedItems

# class OrderForm(forms.ModelForm):
#     class Meta:
#         model = SavedItems
#         fields = []  # No need to specify

class OrderForm(forms.ModelForm):
    products = forms.ModelMultipleChoiceField(queryset=Product.objects.all(), widget=forms.CheckboxSelectMultiple)

    class Meta:
        model = SavedItems
        fields = ['products']