from .models import Products
from django.forms import ModelForm, TextInput, Textarea


class ProductsForm(ModelForm):
    class Meta:
        model = Products
        fields = ["title", "description"]
        widgets = {
            "title": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите наименование'
            }),
            "description": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Введите описание'
            }),
        }
