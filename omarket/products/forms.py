from django import forms
from .models import Products
from .models import Animals
from .models import Cuts
from .models import Pieces
from .models import Price

class corteForm(forms.ModelForm):

    class Meta:
        model = Cuts
        fields = '__all__'

class animalForm(forms.ModelForm):
    
    class Meta:
        model = Animals
        fields = '__all__'
    
class piecesForm(forms.ModelForm):

    class Meta:
        model = Pieces
        fields = '__all__'
        labels = {
            'pieceName':'Nombre'
        }

class productForm(forms.ModelForm):

    class Meta:
        model = Products
        #fields = '__all__'
        fields = {'prodName','quantity', 'exempt', 'description', 'animal_piece', 'animal_product'}
        labels = {
            'prodName':'Nombre',
            'quantity':'Cantidad',
            'exempt':'Exento',
            #'date':'Fecha',
            'description':'Descripción'
        }

class priceForm(forms.ModelForm):

    class Meta:
        model = Price
        fields = {'price', 'price_product'}
        labels = {
            'price':'Precio',
        }