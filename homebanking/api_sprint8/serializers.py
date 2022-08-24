from rest_framework import serializers

from Clientes.models import Cliente, Direccion, Sucursal, TipoCliente, Empleado
from Cuentas.models import Cuenta, Movimientos
from Prestamos.models import Prestamo, TipoPrestamo
from Tarjetas.models import Tarjeta, MarcaTarjeta  

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'
        read_only_fields = ("customer_id",)

class CuentaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cuenta
        fields = ('account_type', 'balance',)
        
class PrestamoSerializer(serializers.ModelSerializer):
    # tipo = serializers.CharField(source='tipo_prestamo.loan_name', read_only=True)  No está definida como fk
    class Meta:
        model = Prestamo
        # fields = ('tipo', 'loan_type','loan_total',)
        fields = ('loan_type','loan_total',)
        
class TarjetaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tarjeta
        fields = '__all__'
        

