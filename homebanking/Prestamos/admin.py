from django.contrib import admin

# Register your models here.
from .models import Prestamo, TipoPrestamo

#Con esta clase ampliamos la configuracion del administrador, extendiendo nuesrta clase propia
#Le decimos que los campos created y updated son de solo lectura
class PrestamoAdmin (admin.ModelAdmin):
    readonly_fields= ()
admin.site.register(Prestamo)
admin.site.register(TipoPrestamo)
