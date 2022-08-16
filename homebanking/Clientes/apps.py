from django.apps import AppConfig


class ClientesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Clientes'

class DireccionConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Direccion'

class SucursalConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Sucursal'

class EmpleadoConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Empleado'

class TipoClientesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'TipoCliente'

