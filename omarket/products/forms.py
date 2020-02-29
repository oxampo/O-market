from django import forms
from .models import Products



class productForm(forms.ModelForm):

    class Meta:
        model = Products
        fields = '__all__'
        labels = {
            'prodName':'Nombre del producto',
            'precio':'Precio',
            'descripcion':'Descipción'
        }