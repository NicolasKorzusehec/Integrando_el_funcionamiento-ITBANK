import os

from django.shortcuts import render, redirect
from django.urls import reverse
#para crear usuarios
from django.contrib.auth.models import User

# el form del registro
from .forms import RegistroForm, ClienteForm, DireccionForm
from Clientes.models import Cliente, Direccion


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
        #No guardamos los datos aqui sino que los almacenamos en la session y los guardamos unicamente cuando tambien se haya creado 
        cliente = Cliente()
        client_form = client_form(data=request.POST)

        if client_form.is_valid():
            interesado = {}
            interesado["customer_name"]= request.POST.get("customer_name", "")
            interesado["customer_surname"] = request.POST.get("customer_surname", "")
            interesado["customer_dni"] = request.POST.get("customer_dni", "")
            interesado["dob"] = request.POST.get("dob", "")
            interesado["email"] = request.POST.get("email", "")
            
            interesado["Telefono"] = request.POST.get("telefono", "")
            
            request.session['interesado'] = interesado 
            request.session.modified = True 
                #{{ request.session.interesado }}   guardo el dato en la session y con este tag lo puedo referenciar desde el front
            print( request.session["interesado"] )

            #cliente.save()
            #print('creado')
            #En lugar de renderizar el template de prestamo hacemos un redireccionamiento enviando una variable OK
        return redirect(reverse('nueva_direccion'))
        
    return render(request, os.path.join("registration","new_client.html"), {'form': client_form})

def NewDirec(request):
    # Se debe crear una instancia de este formulario en la vista 'NewDirec' y enviarla al template
    direc_form = DireccionForm

    #validamos que ocurrio una peticion POST
    if request.method == "POST":
        #Traemos los datos enviados
        direccion = Direccion()
        direc_form = direc_form(data=request.POST)

        if direc_form.is_valid():
            direccion.street = request.POST.get("Calle", "")
            direccion.number = request.POST.get("number", "")
            direccion.city = request.POST.get("city", "")
            direccion.province = request.POST.get("province", "")
            direccion.country = request.POST.get("country", "")
            
            direccion.save()
            print('Direccion creada')

            cliente = Cliente()
            interesado = request.session["interesado"]
            for key in interesado:
                cliente[key]= interesado[key]
            cliente.save()
            print('Cliente creado')

            
            #En lugar de renderizar el template de prestamo hacemos un redireccionamiento enviando una variable OK
        return redirect(reverse('registro'))
        
    return render(request, os.path.join("registration","new_direc.html"), {'form': direc_form})


