import os
from django.shortcuts import render

# Create your views here.
def landing(request):
    """ if request.user.username:
        return render(request, os.path.join("Clientes","home.html"), {'name' : request.user.username}) """
    return render(request, "landing.html")

