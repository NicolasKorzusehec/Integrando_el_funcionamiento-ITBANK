import os

from django.shortcuts import render, redirect
from django.urls import reverse
#para crear usuarios
from django.contrib.auth.models import User

# el form del registro
from .forms import RegistroForm, ClienteForm
from Clientes.models import Cliente


# Create your views here.
def landing(request):
    """ if request.user.username:
        return render(request, os.path.join("Clientes","home.html"), {'name' : request.user.username}) """
    return render(request, "landing.html")

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





def NewClient(request):
    # Se debe crear una instancia de este formulario en la vista 'NewClient' y enviarla al template
    client_form = ClienteForm

    #validamos que ocurrio una peticion POST
    if request.method == "POST":
        #Traemos los datos enviados
        cliente = Cliente()
        client_form = client_form(data=request.POST)

        if client_form.is_valid():
            cliente.customer_name = request.POST.get("customer_name", "")
            cliente.customer_surname = request.POST.get("customer_surname", "")
            cliente.customer_dni = request.POST.get("customer_dni", "")
            cliente.dob = request.POST.get("dob", "")
            
            #print(name,email,content)

            #contacto = Contacto.objects.all(name, email, content)

            cliente.save()
            print('creado')
            #En lugar de renderizar el template de prestamo hacemos un redireccionamiento enviando una variable OK
        return redirect(reverse('nuevo_cliente'))
        
    return render(request, os.path.join("registration","new_client.html"), {'form': client_form})


