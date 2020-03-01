from django.shortcuts import render, redirect
from django.template.loader import get_template
from django.http import HttpResponse
from django.db.utils import IntegrityError
from products.models import Products
from .forms import productForm

# Create your views here.

def productList(request):
    context = {'product_list':Products.objects.all()}
    return render(request, 'product-list.html', context)

def crudProduct(request, id=0):
    if request.method == "GET":
        if id==0:   #Si ID es igual a 0 es una operacion de Crear
            form = productForm()
        else:
            product = Products.objects.get(pk=id) #obten todos los productos donde su primary key sea igual al id
            form = productForm(instance=product)
        return render(request, 'crud-product.html', {'form':form})
    else:
        if id==0:
            form = productForm(request.POST)
        else:
            product = Products.objects.get(pk=id)
            form = productForm(request.POST,instance= product)
        if form.is_valid():
            form.save()
        return redirect('product-list')

    
