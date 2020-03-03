from django.shortcuts import render, redirect
from django.contrib.auth import authenticate,login, logout
from django.contrib.auth.decorators import login_required


#Models

from django.contrib.auth.models import User 
from users.models import Profile

#Excepción
from django.db.utils import IntegrityError


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
        profile.save()

        return redirect('login')

        
    
    return render(request, 'users/signup.html')



def logout_view(request):
    logout(request)
    return redirect('login')

def main(request):
    return render(request,'users/main.html')

def get_all(request):

    if request.method=='POST':
            
        try:
            user = User.objects.get(username=request.POST['username'])
            if  not user.is_staff:

                return render(request, 'users/all_users.html', {'user':user, 'ok':True})

            elif user.is_authenticated and request.POST['username']==user.username:

                return render(request, 'users/all_users.html', {'user':user,'okk':True})

        except:
            return render(request, 'users/all_users.html', {'error':'No hay usuario encontrado'})


        if request.POST['new_username'] != None:
           
            user.first_name = request.POST['new_name']
            user.save(force_update=True)
            
        
    return render(request, 'users/all_users.html')

    