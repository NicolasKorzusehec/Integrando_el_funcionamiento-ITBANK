from django.contrib import admin

from .models import Cuenta
# Register your models here.
class PrestamoAdmin (admin.ModelAdmin):
    readonly_fields= ()
admin.site.register(Cuenta)
