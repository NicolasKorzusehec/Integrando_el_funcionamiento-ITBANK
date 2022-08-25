import os
from django.shortcuts import render, redirect
from django.urls import reverse

from Clientes.models import Cliente

from .forms import PrestamoForm
from .models import Prestamo, TipoPrestamo
from Login.models import Usuario
from Cuentas.models import Cuenta
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
            
            prestamo.loan_preapproval = request.user.customer.customer_type.preapproval_amount

            prestamo.customer = request.user.customer
            prestamo.save()


            cuenta = Cuenta.objects.get(customer_id = request.user.customer)
            monto_preaprobado = int(prestamo.loan_preapproval) 
            monto_total = int(prestamo.loan_total)
            if monto_preaprobado < monto_total:
                request.session["estado_prestamo"] = "El prestamo fue preaprobado, se le notificara como continuar el tramite para alcanzar la totalidad del prestamo solicitado y la documnentacion que debera presentar."

                cuenta.balance = cuenta.balance + prestamo.loan_preapproval
                print(cuenta.balance)
                cuenta.save()

                request.session.modified = True
            elif prestamo.loan_preapproval > prestamo.loan.total:
                request.session["estado_prestamo"] = "El prestamo fue aprobado correctamente."
                request.session.modified = True
 
                cuenta.balance = cuenta.balance + prestamo.loan_total
                cuenta.save()
            
            #Impactamos este monto en la cuenta en pesos del cliente.
        return redirect(reverse('prestamos')) 



    return render(request, os.path.join("Prestamos","prestamos.html"),{'form' : prestamo_form})