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
