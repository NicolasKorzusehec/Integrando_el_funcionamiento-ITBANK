##app_prueba/forms.py
from django import forms

from Clientes.models import TipoCliente, Sucursal
from Cuentas.models import TipoCuenta

#Impacta un nuevo usuario en la BD
class RegistroForm(forms.Form):
    dni = forms.IntegerField(label="DNI", required=True)
    #cliente_id = forms.CharField(label="Nombre de usuario", required=True)
    email = forms.CharField(label="Email", required=True)
    pwd = forms.CharField(label="Contraseña", required=True)
    clave = forms.IntegerField(label="Clave (4 digitos)", required = True)


#Impacta un nuevo Cliente en la BD
class ClienteForm(forms.Form):
    customer_name = forms.CharField(label="Nombre", required=True)
    customer_surname = forms.CharField(label="Apellido", required=True)
    customer_dni = forms.IntegerField(label="DNI", required=True)  # Field name made lowercase.
    dob = forms.DateField(label="Fecha de nacimiento", required=True)
    email = forms.EmailField(label="Email", required=True)
    telefono = forms.IntegerField(label="Telefono", required=True)

    tipocliente = TipoCliente.objects.all()
    typescustomer = []
    for tipo in tipocliente: 
        typescustomer.append((tipo.pk, tipo.type_name))
    customer_type= forms.IntegerField(label='Que tipo de cliente eres?', required=True, widget=forms.Select(choices=typescustomer))


    sucursal = Sucursal.objects.all()
    sucursales = []
    for suc in sucursal: 
        sucursales.append((suc.pk, suc.branch_name))
    branch= forms.IntegerField(label='En que sucursal te adheriste?', required=True, widget=forms.Select(choices=sucursales)) 


class CuentaForm(forms.Form):
    balance = forms.IntegerField(label="Balance", required=True)
    iban = forms.CharField(label="IBAN", required=True)

    tipocuenta = TipoCuenta.objects.all()
    typesaccount = []
    for tipo in tipocuenta: 
        typesaccount.append((tipo.pk, tipo.account_name))

    account_type= forms.IntegerField(label='Que tipo de cuenta quieres?', required=True, widget=forms.Select(choices=typesaccount))



class DireccionForm(forms.Form):
    street = forms.CharField(label="Calle", required=True)
    number = forms.IntegerField(label="Numero", required=True)
    city = forms.CharField(label="Ciudad", required=True)
    province = forms.CharField(label="Provincia", required=True)
    country = forms.CharField(label="Pais", required=True)



"""class DireccionForm(forms.ModelForm):
    class Meta:
        model = Direccion
        fields = ('street', 'number', 'city', 'province', 'country',)
        """


