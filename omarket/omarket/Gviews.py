
from django.shortcuts import render
#from django.template.loader import get_template
#from django.http import HttpResponse
from django.template.loader import get_template
from django.http import HttpResponse

def Home(request):
    
    return render(request, 'home.html')

#vista de compras
def Compras(request): 

    return render(request, 'compras.html')



def QuerysChingones(request):

    return render(request,'QueriesChingones/main.html')


    