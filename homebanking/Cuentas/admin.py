from django.contrib import admin

from .models import Cuenta, Movimientos
# Register your models here.
class CuentaAdmin (admin.ModelAdmin):
    readonly_fields= ()
admin.site.register(Cuenta)
admin.site.register(Movimientos) 
