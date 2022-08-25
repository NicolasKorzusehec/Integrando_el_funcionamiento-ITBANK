import os
from django.shortcuts import render
#importamos el decorador
from django.contrib.auth.decorators import login_required

from Prestamos.models import Prestamo
from Login.models import Usuario
from Clientes.models import Cliente, Sucursal

# Create your views here.
@login_required
def inicio(request):

    #####################################################################33
    suc = 2
    sucursal = Sucursal.objects.get(pk = suc) # Trae la instancia sucursal
    asociados = Cliente.objects.filter(branch = sucursal) # Trae las instancias de clientes por sucursal. branch espera una instancia
    #print ("Asociados: ", asociados)

    prestamos = []

    for cliente in asociados:
        prestamos += Prestamo.objects.filter(customer = cliente)    # Trae las instancias de prestamos por cliente perteneciente a una determinada sucursal. customer espera una instancia
    print (prestamos)
    #####################################################################
    #query que trae una lista de todas las instancias de direccion
    sucursales = Sucursal.objects.all()
    print (sucursales)

    #####################################################################

    return render(request, os.path.join("Clientes","inicio.html"),{'name' : request.user.username})