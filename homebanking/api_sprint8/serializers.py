from rest_framework import serializers

from Clientes.models import Cliente, Direccion, Sucursal, TipoCliente, Empleado
from Cuentas.models import Cuenta, Movimientos
from Prestamos.models import Prestamo, TipoPrestamo
from Tarjetas.models import Tarjeta, MarcaTarjeta  

class ClienteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'
        read_only_fields = ("customer_id",)

class CuentaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Cuenta
        fields = ('account_type', 'balance',)
        
class PrestamoSerializer(serializers.HyperlinkedModelSerializer):
    # tipo = serializers.CharField(source='tipo_prestamo.loan_name', read_only=True)  No está definida como fk
    class Meta:
        model = Prestamo
        # fields = ('tipo', 'loan_type','loan_total',)
        fields = ('loan_type','loan_total',)
        
class TarjetaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tarjeta
        fields = '__all__'
        
class DireccionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Direccion
        fields = '__all__'
        read_only_fields = ("address_id",)
        
class SucursalSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Sucursal
        fields = '__all__'

class ClienteTipoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TipoCliente
        fields = '__all__'

class PrestamoTipoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TipoPrestamo
        fields = '__all__'
        
class MarcaTarjetaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = MarcaTarjeta
        fields = '__all__'