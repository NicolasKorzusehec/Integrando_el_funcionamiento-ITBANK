from django.shortcuts import render

from rest_framework.views import APIView 
from rest_framework.response import Response 
from rest_framework import status

from rest_framework import permissions
# from rest_framework.decorators import api_view
# from rest_framework.reverse import reverse

from Clientes.models import Cliente 
from api_sprint8.serializers import ClienteSerializer 

from Cuentas.models import Cuenta 
from api_sprint8.serializers import CuentaSerializer  

from Prestamos.models import Prestamo 
from api_sprint8.serializers import PrestamoSerializer   

from Tarjetas.models import Tarjeta 
from api_sprint8.serializers import TarjetaSerializer 

from Clientes.models import Direccion 
from api_sprint8.serializers import DireccionSerializer

from Clientes.models import Sucursal 
from api_sprint8.serializers import SucursalSerializer
# Create your views here.

class ClienteDetail(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    def get(self, request, pk):
        cliente = Cliente.objects.filter(pk=pk).first()
        serializer = ClienteSerializer(cliente)
        if cliente:
            return Response(serializer.data, status=status.HTTP_200_OK) 
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)

class ClienteList(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    def get(self, request): 
        clientes = Cliente.objects.all().order_by('customer_id') 
        serializer = ClienteSerializer(clientes, many=True) 
        return Response(serializer.data, status=status.HTTP_200_OK)
    
# Está filtrando por el account id y no por el customer id
class CuentaDetail(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    def get(self, request, pk):
        cuenta = Cuenta.objects.filter(pk=pk).first()
        serializer = CuentaSerializer(cuenta)
        if cuenta:
            return Response(serializer.data, status=status.HTTP_200_OK) 
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)
    
class PrestamoDetail(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    def get(self, request, pk):
        prestamo = Prestamo.objects.filter(pk=pk).first()
        serializer = PrestamoSerializer(prestamo)
        if prestamo:
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)
    
    def delete(self, request, pk): 
        prestamo = Prestamo.objects.filter(pk=pk).first() 
        if prestamo: 
            serializer = PrestamoSerializer(prestamo) 
            prestamo.delete() 
            return Response(serializer.data, status=status.HTTP_200_OK) 
        return Response(status=status.HTTP_404_NOT_FOUND)
    
# Hay que obtener la sucursal a travéz del cliente
class PrestamoList(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    def get(self, request, branch): 
        prestamos = Prestamo.objects.filter(customer_id=branch).order_by('loan_total') 
        serializer = PrestamoSerializer(prestamos, many=True) 
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    # def post(self, request, format=None): 
    #     serializer = PrestamoSerializer(data=request.data) 
    #     if serializer.is_valid(): 
    #         serializer.save() 
    #         return Response(serializer.data, status=status.HTTP_201_CREATED) 
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class TarjetasList(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    def get(self, request, pk):
        tarjetas = Tarjeta.objects.filter(customer_id=pk).order_by('card_id') 
        serializer = TarjetaSerializer(tarjetas, many=True) 
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class DireccionDetail(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    def update(self, instance, validated_data):
        instance.street = validated_data.get('street', instance.street)
        instance.number = validated_data.get('number', instance.number)
        instance.city = validated_data.get('city', instance.city)
        instance.province = validated_data.get('province', instance.province)
        instance.country = validated_data.get('country', instance.country)
        instance.save()
        return instance
        
class SucursalList(APIView):
    def get(self, request):
        sucursales = Sucursal.objects.all().order_by('branch_id') 
        serializer = SucursalSerializer(sucursales, many=True) 
        return Response(serializer.data, status=status.HTTP_200_OK)