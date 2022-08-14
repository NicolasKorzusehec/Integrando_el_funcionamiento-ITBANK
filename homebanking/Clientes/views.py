import os
from django.shortcuts import render

# Create your views here.
def inicio(request):
    return render(request, os.path.join("Clientes","inicio.html"))