from django.shortcuts import render
from django.contrib.auth.models import User 
from users.models import Profile, Addresses
from django.db.utils import IntegrityError
from django.core.exceptions import ObjectDoesNotExist

from products.models import Products

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