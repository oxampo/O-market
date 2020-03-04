from django import forms
from .models import Products
from .models import Animals
from .models import Cuts

class corteForm(forms.ModelForm):

    class Meta:
        model = Cuts
        fields = '__all__'

class animalForm(forms.ModelForm):
    
    class Meta:
        model = Animals
        fields = '__all__'
    


class productForm(forms.ModelForm):

    class Meta:
        model = Products
        fields = '__all__'
        labels = {
            'prodName':'Nombre del producto',
            'precio':'Precio',
            'descripcion':'Descipción'
        }