import os
from django.shortcuts import render
#importamos el decorador
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required
def Prestamos(request):
    return render(request, os.path.join("Prestamos","prestamos.html"),{'name' : request.user.username})