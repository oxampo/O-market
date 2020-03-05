from django.shortcuts import render, redirect
from django.template.loader import get_template
from django.http import HttpResponse
from django.db.utils import IntegrityError
from datetime import datetime
from .models import Products
from .models import Animals
from .models import Cuts
from .models import Pieces
from .models import Price
from .forms import productForm
from .forms import animalForm
from .forms import corteForm
from .forms import piecesForm
from .forms import priceForm

# Create your views here.

def corteList(request):
    context = {'corte_list':Cuts.objects.all()}
    return render(request, 'products/corte-list.html', context)

def crudCorte(request, id=0):
    if request.method == "GET":
        if id==0:   #Si ID es igual a 0 es una operacion de Crear
            form = corteForm()
        else:
            corte = Cuts.objects.get(pk=id) #obten todos los productos donde su primary key sea igual al id
            form = corteForm(instance=corte)
        return render(request, 'products/crud-corte.html', {'form':form})
    else:
        if id==0:
            form = corteForm(request.POST)
            validar = form['cutName'].value()
            cortes = Cuts.objects.all()
            for cut in cortes:
                if validar == cut.cutName:
                    #return render(request, 'products/crud-corte.html', {'form':form}, {'error':'ERROR: Este aatributo ya fue creado'})
                    return redirect('corte-list')
        else:
            corte = Cuts.objects.get(pk=id)
            form = corteForm(request.POST,instance= corte)
        if form.is_valid():
            form.save()

        return redirect('corte-list')

def animalList(request):
    context = {'animal_list':Animals.objects.all()}
    return render(request, 'products/animal-list.html', context)


def crudAnimal(request, id=0):
    if request.method == "GET":
        if id==0:   #Si ID es igual a 0 es una operacion de Crear
            form = animalForm()
        else:
            animal = Animals.objects.get(pk=id) #obten todos los productos donde su primary key sea igual al id
            form = animalForm(instance=animal)
        return render(request, 'products/crud-animal.html', {'form':form})
    else:
        if id==0:
            form = animalForm(request.POST)
        else:
            animal = Animals.objects.get(pk=id)
            form = animalForm(request.POST,instance= animal)
        if form.is_valid():
            form.save()
        return redirect('animal-list')

def pieceList(request):
    context = {'pieza_list':Pieces.objects.all()}
    return render(request, 'products/piece-list.html', context)

def crudPiece(request, id=0):
    if request.method == "GET":
        if id==0:   #Si ID es igual a 0 es una operacion de Crear
            form = piecesForm()
        else:
            pieza = Pieces.objects.get(pk=id) #obten todos los productos donde su primary key sea igual al id
            form = piecesForm(instance=pieza)
        return render(request, 'products/crud-piece.html', {'form':form})
    else:
        if id==0:
            form = piecesForm(request.POST)
        else:
            pieza = Pieces.objects.get(pk=id)
            form = piecesForm(request.POST,instance= pieza)
        if form.is_valid():
            form.save()
        return redirect('piece-list')

def productList(request):
    context = {'product_list':Products.objects.all()}
    return render(request, 'products/product-list.html', context)

def crudProduct(request, id=0):
    if request.method == "GET":
        if id==0:   #Si ID es igual a 0 es una operacion de Crear
            form = productForm()
        else:
            product = Products.objects.get(pk=id) #obten todos los productos donde su primary key sea igual al id
            form = productForm(instance=product)
        return render(request, 'products/crud-product.html', {'form':form})
    else:
        if id==0:
            form = productForm(request.POST)
        else:
            product = Products.objects.get(pk=id)
            form = productForm(request.POST,instance= product)
        if form.is_valid():
            form.save()
        return redirect('product-list')

def precioList(request):
    context = {'price_list':Price.objects.all()}
    return render(request, 'products/precios-list.html', context)

def asignarPrecio(request, id=0):
    if request.method == "GET":
        if id==0:   #Si ID es igual a 0 es una operacion de Crear
            form = priceForm()
        else:
            price = Price.objects.get(pk=id) #obten todos los productos donde su primary key sea igual al id
            form = priceForm(instance=price)
        return render(request, 'products/asignar-precio.html', {'form':form})
    else:
        if id==0:
            form = priceForm(request.POST)
        else:
            price = Price.objects.get(pk=id)
            form = priceForm(request.POST,instance= price)
        if form.is_valid():
            form.save()
        return redirect('precios-list')
