from django.contrib import admin

from .models import Tarjeta, MarcaTarjeta

# Register your models here.


class ProjectAdmin (admin.ModelAdmin):
    readonly_fields= ()
admin.site.register(Tarjeta)
admin.site.register(MarcaTarjeta)
