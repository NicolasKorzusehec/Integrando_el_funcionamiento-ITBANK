from django.shortcuts import render

# Create your views here.
def landing(request):
    return render(request, "landing.html")

def iniciar(request):
    return render(request, "login.html")