from django import forms

class solicitudPrestamo(forms.Form):
    tipoPrestamo = forms.CharField(label="Tipo  ", required=True)
    fechaInicio = forms.DecimalField(label="fecha de inicio",required=True,widget= forms.DateTimeInput())
    monto = forms.DecimalField(label="Monto solicitado ", required=True)
