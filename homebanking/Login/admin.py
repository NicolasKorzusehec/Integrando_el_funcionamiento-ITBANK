from django.contrib import admin

# Register your models here.
from django.contrib.auth.admin import UserAdmin
from .models import UsuarioCustom

admin.site.register(UsuarioCustom, UserAdmin)