import os
from django.shortcuts import render, redirect
from django.urls import reverse

from Clientes.models import Cliente

from .forms import PrestamoForm
from .models import Prestamo, TipoPrestamo
from Login.models import Usuario
#importamos el decorador
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required
def Prestamos(request):
    prestamo_form=PrestamoForm

    if request.method == "POST":
        #Traemos los datos enviados
        prestamo = Prestamo()
        prestamo_form = prestamo_form(data=request.POST)

        if prestamo_form.is_valid():
            for field in prestamo._meta.get_fields():
                field = field.name #guardamos solo el nombre del campo
                if request.POST.get(field, "") != "":
                    value = request.POST.get(field, "")
                    if field == "loan_type":
                        value = request.POST.get(field, "")
                        tipo = TipoPrestamo.objects.get(pk = value)
                        setattr(prestamo, field, tipo) 
                    else:
                        setattr(prestamo, field, value)  
            
            prestamo.customer = request.user.customer
            prestamo.save()
        return redirect(reverse('prestamos')) 



    return render(request, os.path.join("Prestamos","prestamos.html"),{'form' : prestamo_form})