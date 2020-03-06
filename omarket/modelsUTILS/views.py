from django.shortcuts import render, redirect
from django.template.loader import get_template
from django.http import HttpResponse
from django.db.utils import IntegrityError
from django.contrib.auth.models import User 
from users.models import Profile, Addresses
from django.core.exceptions import ObjectDoesNotExist
from .models import Puzzle
from products.models import Products
from .forms import puzzleForm

# Create your views here.

def VentasMain(request):
    return render(request,'ventas/main.html')


def Vender(request):
    data = {}
    if request.method=='POST':
        #validación para ver si el usuario existe; si existe, se compra
        if request.POST.get('cedula') or request.POST.get('product'):
            if request.POST.get('cedula') and not request.POST.get('product'):
                cedula = request.POST.get('cedula')

                if not int(cedula)>0:
                        return render(request,'ventas/vender.html',{'error':'cédula no válida ({} es negativo)'.format(cedula)})
        try:
            cedula = request.POST.get('cedula')
            print("cedulaaa")
            print(cedula)
            profile = Profile.objects.get(cedula=int(cedula))
            user = User.objects.get(profile=profile)
            data['nombre'] =user.first_name
            data['apellido'] =user.last_name
            cedula = request.POST['cedula']
            data['cedula'] =profile.cedula
        except:      
            return render(request,'ventas/vender.html',{'error':'no existe perfil/usuario de cédula {}. Debe registrarlo'.format(cedula)})
            

        if request.POST.get('product'):
            product = request.POST.get('product')
            return render(request,'ventas/vender.html', {'data':data,'ready':True, 'productsSel':product,'cedula':request.POST['cedula']}) 
            
            if request.POST.get('pago'):
                print(request.POST.get('pago'))
                data['pago']=request.POST['pago']
                print(data)

        all_products = Products.objects.all()

        return render(request,'ventas/vender.html', {'data':data,'ready':True,'products':all_products, 'cedula':cedula})                

        
        #elif request.POST.get('pago'):
        #    data['pago']=request.POST['pago']
        #    print(data)
        #return render(request,'ventas/vender.html', {'data':data,'ready':True, 'products':all_products})
        
        
    return render(request,'ventas/vender.html')



def Ordenes(request):


    return render(request, 'ventas/orders.html')

def puzzleList(request):
    context = {'puzzle_list':Puzzle.objects.all()}
    return render(request, 'puzzles/puzzles-list.html', context)

def puzzlesCrud(request, id=0):

    if request.method == "GET":
        if id==0:   #Si ID es igual a 0 es una operacion de Crear
            form = puzzleForm()
        else:
            puzzle = Puzzle.objects.get(pk=id) #obten todos los productos donde su primary key sea igual al id
            form = puzzleForm(instance=puzzle)
            #form = puzzleForm()
        return render(request, 'puzzles/crud-puzzles.html', {'form':form})
    else:
        if id==0:
            form = puzzleForm(request.POST)
            validar = form['enunciado'].value()
            puzzles = Puzzle.objects.all()
            for puzzle in puzzles:
                if validar == puzzle.cutName:
                    #return render(request, 'products/crud-corte.html', {'form':form}, {'error':'ERROR: Este aatributo ya fue creado'})
                    return redirect('puzzle-list')
        else:
            puzzle = Puzzle.objects.get(pk=id)
            form = puzzleForm(request.POST,instance= puzzle)
            #form = puzzleForm(request.POST)
        if form.is_valid():
            form.save()

        return redirect('puzzle-list')
