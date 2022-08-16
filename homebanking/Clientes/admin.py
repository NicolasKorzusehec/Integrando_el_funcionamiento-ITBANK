from django.contrib import admin

# Register your models here.

#Todavía no se ve la tabla proyecto que creamos, porque no la registramos en el admin de nuestra app Clientes.

from .models import Cliente, Direccion, Sucursal, Empleado, TipoCliente

#Con esta clase ampliamos la configuracion del administrador, extendiendo nuesrta clase propia
#Le decimos que los campos created y updated son de solo lectura
class ProjectAdmin (admin.ModelAdmin):
    readonly_fields= ('created','updated')
admin.site.register(Cliente)
admin.site.register(Direccion)
admin.site.register(Sucursal)
admin.site.register(Empleado)
admin.site.register(TipoCliente)
