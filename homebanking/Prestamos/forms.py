from django import forms

from .models import TipoPrestamo

class solicitudPrestamo(forms.Form):
    tipoprestamo = TipoPrestamo.objects.all()
    tipos = []
    pos = 1
    for tipo in tipoprestamo: 
        tipos.append((pos, tipo.loan_name))
        pos += 1 

    loan_type= forms.IntegerField(label='Que tipo de prestamo desea?', required=True, widget=forms.Select(choices=tipos))

    fechaInicio = forms.DateField(label="Fecha de inicio",required=True,widget= forms.DateTimeInput())
    monto = forms.DecimalField(label="Monto solicitado ", required=True)
