from django.shortcuts import render

from rest_framework.views import APIView 
from rest_framework.response import Response 
from rest_framework import status

from rest_framework import permissions
from rest_framework.decorators import api_view
from rest_framework.reverse import reverse

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

from Clientes.models import TipoCliente 
from api_sprint8.serializers import ClienteTipoSerializer

from Prestamos.models import TipoPrestamo 
from api_sprint8.serializers import PrestamoTipoSerializer

from Tarjetas.models import MarcaTarjeta 
from api_sprint8.serializers import MarcaTarjetaSerializer

from Cuentas.models import TipoCuenta
from api_sprint8.serializers import TipoCuentaSerializer
# Create your views here.

class ClienteDetail(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    def get(self, request, pk):
        cliente = Cliente.objects.filter(pk=pk).first()
        serializer = ClienteSerializer(cliente, context={'request': request})
        if cliente:
            return Response(serializer.data, status=status.HTTP_200_OK) 
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)

class ClienteList(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    def get(self, request): 
        clientes = Cliente.objects.all().order_by('customer_id') 
        serializer = ClienteSerializer(clientes, many=True, context={'request': request}) 
        return Response(serializer.data, status=status.HTTP_200_OK)
    
# Está filtrando por el account id y no por el customer id
class CuentaDetail(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    def get(self, request, pk):
        cuenta = Cuenta.objects.filter(pk=pk).first()
        serializer = CuentaSerializer(cuenta, context={'request': request})
        if cuenta:
            return Response(serializer.data, status=status.HTTP_200_OK) 
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)
    
class CuentaList(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    def get(self, request): 
        cuentas = Cuenta.objects.all().order_by('customer_id') 
        serializer = CuentaSerializer(cuentas, many=True, context={'request': request}) 
        return Response(serializer.data, status=status.HTTP_200_OK)    
    
class PrestamoDetail(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    def get(self, request, pk):
        prestamo = Prestamo.objects.filter(pk=pk).first()
        serializer = PrestamoSerializer(prestamo, context={'request': request})
        if prestamo:
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)
    
    def delete(self, request, pk): 
        prestamo = Prestamo.objects.filter(pk=pk).first() 
        if prestamo: 
            serializer = PrestamoSerializer(prestamo, context={'request': request}) 
            prestamo.delete() 
            return Response(serializer.data, status=status.HTTP_200_OK) 
        return Response(status=status.HTTP_404_NOT_FOUND)
    

class PrestamoList(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    def get(self, request): 
        prestamos = Prestamo.objects.all().order_by('loan_id') 
        serializer = PrestamoSerializer(prestamos, many=True, context={'request': request}) 
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request, format=None): 
        serializer = PrestamoSerializer(data=request.data, context={'request': request}) 
        if serializer.is_valid(): 
            serializer.save() 
            return Response(serializer.data, status=status.HTTP_201_CREATED) 
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class PrestamoSucursalList(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    def get(self, request, pk): 
        sucursal = Sucursal.objects.filter(pk=pk).first()
        asociados = Cliente.objects.filter(branch = sucursal).order_by('customer_id')
        prestamos = []
        for cliente in asociados:
            prestamos += Prestamo.objects.filter(customer = cliente)
        serializer = PrestamoSerializer(prestamos, many=True, context={'request': request}) 
        return Response(serializer.data, status=status.HTTP_200_OK)

class TarjetasList(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    def get(self, request, pk):
        tarjetas = Tarjeta.objects.filter(customer_id=pk).order_by('card_id') 
        serializer = TarjetaSerializer(tarjetas, many=True, context={'request': request}) 
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class DireccionDetail(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    
    def put(self, request, pk): 
        direccion = Direccion.objects.filter(pk=pk).first() 
        serializer = DireccionSerializer(direccion, data=request.data, context={'request': request}) 
        if serializer.is_valid(): 
            serializer.save()
            return Response(serializer.data) 
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def get(self, request, pk):
        direccion = Direccion.objects.filter(pk=pk).order_by('address_id') 
        serializer = DireccionSerializer(direccion, many=True,context={'request': request}) 
        return Response(serializer.data, status=status.HTTP_200_OK)

class DireccionList(APIView):
    def get(self, request):
        direcciones = Direccion.objects.all().order_by('address_id') 
        serializer = DireccionSerializer(direcciones, many=True, context={'request': request}) 
        return Response(serializer.data, status=status.HTTP_200_OK)
   
class SucursalList(APIView):
    def get(self, request):
        sucursales = Sucursal.objects.all().order_by('branch_id') 
        serializer = SucursalSerializer(sucursales, many=True, context={'request': request}) 
        return Response(serializer.data, status=status.HTTP_200_OK)
    
@api_view(['GET']) 
def api_root(request, format=None):
    return Response({ 
                     'clientes': reverse('clientes-list', request=request, format=format), 
                     'cuentas': reverse('cuentas-list', request=request, format=format),
                     'prestamos': reverse('prestamos-list', request=request, format=format),
                     'direcciones': reverse('direccion-list', request=request, format=format),
                     'sucursales': reverse('sucursales-list', request=request, format=format)
                     })
    
class SucursalDetail(APIView):
    def get(self, request, pk):
        sucursal = Sucursal.objects.filter(pk=pk).order_by('branch_id') 
        serializer = SucursalSerializer(sucursal, many=True, context={'request': request}) 
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class ClienteTipoDetail(APIView):
    def get(self, request, pk):
        tipo_cliente = TipoCliente.objects.filter(pk=pk).order_by('customer_type_id') 
        serializer = ClienteTipoSerializer(tipo_cliente, many=True, context={'request': request}) 
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class TipoPrestamoDetail(APIView):
    def get(self, request, pk):
        tipo_prestamo = TipoPrestamo.objects.filter(pk=pk).order_by('type_id') 
        serializer = PrestamoTipoSerializer(tipo_prestamo, many=True, context={'request': request}) 
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class TarjetasDetail(APIView):
    def get(self, request, pk):
        tarjeta = Tarjeta.objects.filter(pk=pk).order_by('card_id') 
        serializer = TarjetaSerializer(tarjeta, many=True, context={'request': request}) 
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class MarcaTarjetaDetail(APIView):
    def get(self, request, pk):
        marca = MarcaTarjeta.objects.filter(pk=pk).order_by('card_id') 
        serializer = MarcaTarjetaSerializer(marca, many=True, context={'request': request}) 
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class TipoCuentaDetail(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    def get(self, request, pk):
        cuenta_tipo = TipoCuenta.objects.filter(pk=pk).first()
        serializer = TipoCuentaSerializer(cuenta_tipo, context={'request': request})
        if cuenta_tipo:
            return Response(serializer.data, status=status.HTTP_200_OK) 
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)