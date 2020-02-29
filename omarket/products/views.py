from django.shortcuts import render, redirect
from django.template.loader import get_template
from django.http import HttpResponse
from django.db.utils import IntegrityError
from products.models import Products
from .forms import productForm

# Create your views here.


def crudProduct(request):
    if request.method == "GET":
        form = productForm()
        return render(request, 'crud-product.html', {'form':form})
    else:
        form = productForm(request.POST)
        if form.is_valid():
            form.save()
        return render(request, 'crud-product.html', {'form':form})

    
