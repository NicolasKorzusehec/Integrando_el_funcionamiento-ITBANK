Ejecucion para levantar el proyecto desde un codespace de github. Valido para programar desde una tablet,

1. Descargo dependencias

1. accedo desde la consola bash a la carpeta que inicializa el proyecto
Ver los Directorios y archivos en la ubicacion actual: 
ls -a
Entrar al directorio: 
cd (nombre de la carpeta)
volver para atras:
cd ..

Ubicacion:
/workspace/Integrando_el_funcionamiento-ITBANK/homebanking

1. Ejecuto 
python manage.py runserver

Seguro figura un error con las migraciones, en principio solucionarlo por el camino facil
python manage.py makemigration
python manage.py migrate

Capaz hay que aplicar el comando mas de una vez. Una vez que se solucionaron las migraciones correr la ejecucion denuevo.

1. Detener Programa
ctrl + C

1. Crear usuario administrador
python manage.py createsuperuser

1. Ingresar a la pestaña de administracion
Al final de la url de la app una vez que se inicio agregar:
/admin

Desde aqui con el super user completar la informacion del superusuario, valida para el login.

Super usuario propuesto: 
Nombre: ITBA
Correo: nkorzusehec@gmail.com
Contraseña: 1234
Clave: 123


## Problema con la verifiacion CSRF, con el debug false se soluciona pero no puedo correr la app.
Tiene que ver con la url del codespace

Posible solucion:
Add this line to your settings.py. This was not required when I was using 3.2 and now I can't POST a form containing a CSRF without it.

Review this line for any changes needed, for example if you need to swap out https for http.

Root cause is the addition of origin header checking in 4.0.

https://docs.djangoproject.com/en/4.0/ref/settings/#csrf-trusted-origins

