import os
from django.shortcuts import render
#importamos el decorador
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required
def inicio(request):
    return render(request, os.path.join("Clientes","inicio.html"),{'name' : request.user.username})