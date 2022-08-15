"""homebanking URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls import include


from Login import views as login_views
from Clientes import views as clients_views

urlpatterns = [
    path('', login_views.landing, name="landing"),
    path('inicio/', clients_views.inicio, name="inicio"),

    path('admin/', admin.site.urls),


    #Agregamos las direcciones de autenticacion (login, logout, gestion password)
    path('accounts/',include('django.contrib.auth.urls')),
    #path('accounts/registro', pruebas_views.registro,name = "registro"),
    path('logout/', login_views.logout, name="logout"),
    path('accounts/registro', login_views.registro,name = "registro"),

]


##Los archivos que sube un usuario a través del administrador, no se consideran recursos estáticos, se denominan archivos multimedia Para poder cargar y después referir archivos de este tipo, necesitamos crear una carpeta donde almacenar estos recursos.
#La llamamos media y la creamos en la raíz de nuestro proyecto
#Luego en el archivo settings.py y abajo de todo añadimos dos variables, una para indicar la URL externa y otra para la carpeta interna donde se encuentran los archivos media.

##Si queremos ver la imagen en nuestro servidor de desarrollo, tenemos que editar nuestro archivo urls.py, en este caso se usara solo en modo debug.
#Como resultado, Podemos crear un proyecto en nuestra herramienta de gestión de portfolio de forma completa, modificarlo y visualizarlo.
from django.conf import settings
if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
