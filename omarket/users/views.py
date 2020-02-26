from django.shortcuts import render, redirect
from django.contrib.auth import authenticate,login, logout
from django.contrib.auth.decorators import login_required


#Models

from django.contrib.auth.models import User 
from users.models import Profile

#Excepción
from django.db.utils import IntegrityError


# Create your views here.
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


@login_required
def logout_view(request):
    logout(request)
    return redirect('login')



    