import os

from django.shortcuts import render, redirect
from django.urls import reverse
#para crear usuarios
from Login.models import Usuario

# el form del registro
from .forms import RegistroForm, ClienteForm, DireccionForm
from Clientes.models import Cliente, Direccion


# Create your views here.
def landing(request):
    return render(request, "landing.html")

def registro(request):
    registro_form = RegistroForm

    if request.method == "POST":
        #Traemos los datos enviados
        registro_form = registro_form(data=request.POST)
        #Chequeamos que los datos son validos, de ser asi, los asignamos a una variable
        if registro_form.is_valid():
            interesado = {}
            for field in registro_form:
                field = field.name
                resultado = request.POST.get(field, "")
                if resultado != "":
                    interesado[field]= resultado  
            
            dni= interesado["dni"]
            condicion = Cliente.objects.filter(customer_dni = dni)
            if str(condicion) != "<QuerySet []>":
                print(condicion) 
                cliente_id = request.POST.get('dni','')
                email = request.POST.get('email','')
                pwd = request.POST.get('pwd','') 
                clave = request.POST.get("clave",'')
                print(cliente_id,email,pwd) 

                user = Usuario.objects.create_user(cliente_id, email, pwd, clave)
                user.save()
                print('creado')
            else:
                return redirect(reverse('nuevo_cliente'))
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
            interesado = {}  #almacena la informacion del aspirante y sera guardada en la session en curso.

            for field in cliente._meta.get_fields():
                field = field.name #guardamos solo el nombre del campo
                if request.POST.get(field, "") != "":
                    interesado[field] = request.POST.get(field, "")
            request.session['interesado'] = interesado 
            request.session.modified = True  
                #{{ request.session.interesado }}   guardo el dato en la session y con este tag lo puedo referenciar desde el front
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
            for field in direccion._meta.get_fields():
                field = field.name #guardamos solo el nombre del campo
                resultado = request.POST.get(field, "")
                if resultado != "":
                    setattr(direccion, field, resultado)   
            direccion.save()
            #print('Direccion creada: ', direccion)

            cliente = Cliente()
            interesado = request.session["interesado"] 
            for key in interesado:
                setattr(cliente, key, interesado[key]) 
            cliente.save() 
            #print('Cliente creado: ', cliente) 

            request.session["interesado"] = "" 
            request.session.modified = True   
 
            #En lugar de renderizar el template de prestamo hacemos un redireccionamiento enviando una variable OK
        return redirect(reverse('registro'))
        
    return render(request, os.path.join("registration","new_direc.html"), {'form': direc_form})


