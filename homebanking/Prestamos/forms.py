from django import forms

from .models import TipoPrestamo

class PrestamoForm(forms.Form):
    tipoprestamo = TipoPrestamo.objects.all()
    tipos = []
    pos = 1
    for tipo in tipoprestamo: 
        tipos.append((pos, tipo.loan_name))
        pos += 1 

    loan_type= forms.IntegerField(label='Que tipo de prestamo desea?', required=True, widget=forms.Select(choices=tipos))

    loan_date = forms.DateField(label="Fecha de inicio",required=True,widget= forms.DateTimeInput())
    loan_total = forms.DecimalField(label="Monto solicitado ", required=True)
