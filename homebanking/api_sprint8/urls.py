from django.contrib import admin
from django.urls import path

from api_sprint8 import views

urlpatterns = [
        path('', views.api_root),
        path('clientes/', views.ClienteList.as_view(), name='clientes-list'),
        path('clientes/<int:pk>/', views.ClienteDetail.as_view(), name='cliente-detail'),
        path('cuenta/<int:pk>/', views.CuentaDetail.as_view()),
        path('prestamo/<int:pk>/', views.PrestamoDetail.as_view()),
        path('prestamos/<int:branch>', views.PrestamoList.as_view()),
        path('tarjetas/<int:pk>/', views.TarjetasList.as_view()),
        path('direccion/<int:pk>/', views.DireccionDetail.as_view(), name='direccion-detail'),
        path('sucursales/', views.SucursalList.as_view(), name='sucursales-list'),
        
        path('clientes-tipo/<int:pk>/', views.ClienteTipoDetail.as_view(), name='tipocliente-detail'),
        path('sucursales/<int:pk>/', views.SucursalDetail.as_view(), name='sucursal-detail'),
    ]