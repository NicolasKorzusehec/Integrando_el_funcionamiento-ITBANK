from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
# Register your models here.
#from django.contrib.auth.admin import UserAdmin
from .models import Usuario

class UserAdmin(BaseUserAdmin):
    list_display = ('username', 'first_name', 'last_name', 'email', 'is_active', 'is_staff', 'is_superuser')
    list_filter = ('is_admin',)
 
    fieldsets = (
        (None, {'fields': ('username', 'email', 'password','first_name','last_name', 'telefono', 'clave', 'customer')}),
        ('Permissions', {'fields': ('is_admin', 'is_staff','is_active', 'is_superuser')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2'),
        }),
    )

    search_fields = ('username',)
    ordering = ('username',)
    filter_horizontal = ()



admin.site.register(Usuario, UserAdmin)