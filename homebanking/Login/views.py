import os

from django.shortcuts import render, redirect
from django.urls import reverse
#para crear usuarios
from django.contrib.auth.models import User

# el form del registro
from .forms import RegistroForm

# Create your views here.
def landing(request):
    """ if request.user.username:
        return render(request, os.path.join("Clientes","home.html"), {'name' : request.user.username}) """
    return render(request, "landing.html")

def logout(request):
    """ if request.user.username:
        return render(request, os.path.join("Clientes","home.html"), {'name' : request.user.username}) """
    return render(request, os.path.join("registration","logout.html"))

def registro(request):
    registro_form = RegistroForm

    if request.method == "POST":
        #Traemos los datos enviados
        registro_form = registro_form(data=request.POST)
        #Chequeamos que los datos son validos, de ser asi, los asignamos a una variable
        if registro_form.is_valid():
            cliente_id= request.POST.get('cliente_id','')
            email = request.POST.get('email','')
            pwd = request.POST.get('pwd','')
            print(cliente_id,email,pwd)

            user = User.objects.create_user(cliente_id, email, pwd)
            user.save()
            print('creado')
        #En lugar de renderizar el template de prestamo hacemos un redireccionamiento enviando una variable OK
        return redirect(reverse('login'))
    
    return render(request, os.path.join("registration","registro.html"),{'form': registro_form})
