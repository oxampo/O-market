from django.shortcuts import render
from django.contrib.auth.models import User 
from users.models import Profile, Addresses
from django.db.utils import IntegrityError
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.

def VentasMain(request):
    return render(request,'ventas/main.html')



def Vender(request):

    if request.method=='POST':
        #validación para ver si el usuario existe; si existe, se compra
       
        cedula = request.POST.get('cedula')

        if not int(cedula)>0:
                return render(request,'ventas/vender.html',{'error':'cédula no válida ({} es negativo)'.format(cedula)})
        try:
            profile = Profile.objects.get(cedula=int(cedula))
        except:      
            return render(request,'ventas/vender.html',{'error':'no existe perfil/usuario de cédula {}. Debe registrarlo'.format(cedula)})
        
        user = User.objects.get(profile=profile)
        data = {'nombre':user.first_name, 'apellido':user.last_name,'cedula':profile.cedula}

        return render(request,'ventas/vender.html', {'data':data,'ready':True})
        
        
    return render(request,'ventas/vender.html')



def Ordenes(request):


    return render(request, 'ventas/orders.html')