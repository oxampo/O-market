from django.shortcuts import render, redirect
from django.template.loader import get_template
from django.http import HttpResponse
from django.db.utils import IntegrityError
from .models import Products
from .models import Animals
from .models import Cuts
from .forms import productForm
from .forms import animalForm
from .forms import corteForm

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

    
