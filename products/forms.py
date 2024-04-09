from django import forms
from .models import Products,Category

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields= '__all__'

class ProductForm(forms.ModelForm):
    class Meta:
        model = Products
        exclude = ('created_at',)