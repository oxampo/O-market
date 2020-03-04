from django.shortcuts import render, redirect
from django.contrib.auth import authenticate,login, logout
from django.contrib.auth.decorators import login_required


#Models

from django.contrib.auth.models import User 
from users.models import Profile

#Excepción
from django.db.utils import IntegrityError
from django.core.exceptions import ObjectDoesNotExist



# Create your views here.
"""
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request,username=username, password = password)
        
        if user:
            login(request,user)
            return redirect('home')
        else:
            return render(request, 'users/login.html',{'error':'Nombre de usuario o contraseña incorrecta'})
    return render(request, 'users/login.html')
"""

def signup(request):

    if request.method=='POST':
        username = request.POST['username']
        passwd = request.POST['passwd']
        passwd_confirmation = request.POST['passwd_confirmation']

        if passwd != passwd_confirmation:
            return render(request, 'users/signup.html',{'error':'Confimación de contraseña no coincide'})
    
        #Query para crear un usuario (try and except es por si se el username ya está en uso)
        try:
            user = User.objects.create_user(username=username, password=passwd)
        except IntegrityError:
            return render(request, 'users/signup.html',{'error':'Nombre de usuario ya en uso'})
        
        user.first_name=request.POST['first_name']
        user.last_name=request.POST['last_name']
        user.email=request.POST['email']
        user.save()

        profile = Profile(user=user)
        profile.cedula = request.POST['cedula']
        profile.save()

    
    return render(request, 'users/signup.html')



def logout_view(request):
    logout(request)
    return redirect('login')

def main(request):
    return render(request,'users/main.html')


user = None

def modify_user(request):


    if request.method=='POST':

        try:
            if request.POST.get('username') and not request.POST.get('username') == None:
                print("se mandó nombre")
                user = User.objects.get(username=request.POST['username'])
                if  not user.is_staff:
                    print(user)
                    profile = Profile.objects.get(user=user)
                    print(profile.address)
                    return render(request, 'users/modify_user.html', {'user':user, 'profile':profile, 'ok':True})
                elif user.is_authenticated and request.POST['username']==user.username:
                    print(user)
                    return render(request, 'users/modify_user.html', {'user':user,'okk':True})

        except:
            return render(request, 'users/modify_user.html', {'error':'No hay usuario encontrado'})



        try:
            if request.POST.get('newname') or request.POST.get('newlname') or request.POST.get('newemail'):
                print("entró")
                #print({{request.POST['newname'] | default_if_none:"nothing"}})
                print(request.POST['newlname'])
                print(request.POST.get('newemail'))
                user = User.objects.get(id=request.POST['userid'])
                user.first_name = request.POST['newname']
                user.last_name = request.POST.get('newlname')
                user.email = request.POST.get('newemail')
                user.save()

                if  not user.is_staff:
                    if request.POST.get('newcedula') or request.POST.get('newaddress'): 
                        if int(request.POST.get('newcedula'))>0:
                            try:
                                profile_x = Profile.objects.get(cedula=request.POST.get('newcedula')) 
                                if profile_x: 
                                    return render(request, 'users/modify_user.html',{'error':'Número de cédula ya en uso'})
                                else: 
                                    pass
                            except ObjectDoesNotExist:

                                    profile.cedula = request.POST.get('newcedula')
                                    profile = Profile.objects.get(user=user)
                                    profile.address = request.POST.get('newaddress')
                                    profile.save()
                        else:
                            return render(request, 'users/modify_user.html',{'error':'la cédula debe ser positiva'})

            return render(request, 'users/modify_user.html',{'ready':'usuario modificado','user':user, 'ok':True, 'okk':True})

        except KeyError:
            return render(request, 'users/modify_user.html',{'error':'no fue para el baile'})
        
    return render(request, 'users/modify_user.html',{'no':True})

def get_all(request):
    users = User.objects.all()

    return render(request,'users/all.html',{'users':users})

    