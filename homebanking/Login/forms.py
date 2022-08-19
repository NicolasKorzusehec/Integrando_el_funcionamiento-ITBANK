##app_prueba/forms.py
from django import forms

from Clientes.models import Direccion

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

    """
    customer_type = forms.IntegerField(label="customer_type", required=True)
    customer_address = forms.IntegerField(label="customer_type", required=True)
    branch = forms.IntegerField(label="customer_type", required=True)

    lista=[('A','30 Cuotas'),  ('B','60 Cuotas'), ('C', '90 Cuotas')]
    item_lista= forms.CharField(label='Que opciones elegis?', widget=forms.Select(choices=lista))"""



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


