from django.contrib import admin

# Register your models here.
from .models import Prestamo

#Con esta clase ampliamos la configuracion del administrador, extendiendo nuesrta clase propia
#Le decimos que los campos created y updated son de solo lectura
class ProjectAdmin (admin.ModelAdmin):
    readonly_fields= ('loan_type', 'customer')
admin.site.register(Prestamo)
