from django.contrib import admin
from django.urls import path

from api_sprint8 import views

urlpatterns = [
        path('clientes/', views.ClienteList.as_view()),
        path('clientes/<int:pk>/', views.ClienteDetail.as_view()),
        path('cuenta/<int:pk>/', views.CuentaDetail.as_view()),
        path('prestamo/<int:pk>/', views.PrestamoDetail.as_view()),
        path('prestamos/<int:branch>', views.PrestamoList.as_view()),
        path('tarjetas/<int:pk>/', views.TarjetasList.as_view()),
        path('direccion/', views.DireccionDetail.as_view()),
        path('sucursales/', views.SucursalList.as_view()),
    ]