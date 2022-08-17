##app_prueba/forms.py
from django import forms

class RegistroForm(forms.Form):
    cliente_id = forms.CharField(label="cliente_id", required=True)
    email = forms.CharField(label="email", required=False)
    pwd = forms.CharField(label="pwd", required=False)


class ClienteForm(forms.Form):
    customer_name = forms.CharField(label="customer_name", required=True)
    customer_surname = forms.CharField(label="customer_surname", required=True)
    customer_dni = forms.IntegerField(label="customer_dni", required=True)  # Field name made lowercase.
    dob = forms.DateField(label="dob", required=True)
    
    
    """customer_type = forms.IntegerField(label="customer_type", required=True)
    customer_address = forms.IntegerField(label="customer_type", required=True)
    branch = forms.IntegerField(label="customer_type", required=True)

    lista=[('A','30 Cuotas'),  ('B','60 Cuotas'), ('C', '90 Cuotas')]
    item_lista= forms.CharField(label='Que opciones elegis?', widget=forms.Select(choices=lista))"""



