
from django.shortcuts import render
#from django.template.loader import get_template
#from django.http import HttpResponse

def Home(request):
    
    return render(request, 'home.html')


def QuerysChingones(request):

    return render(request,'QueriesChingones/main.html')


    