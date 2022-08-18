import os
from django.shortcuts import render
from .forms import solicitudPrestamo
#importamos el decorador
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required
def Prestamos(request):
    solicitud_Prestamo=solicitudPrestamo
    return render(request, os.path.join("Prestamos","prestamos.html"),{'form' : solicitud_Prestamo})