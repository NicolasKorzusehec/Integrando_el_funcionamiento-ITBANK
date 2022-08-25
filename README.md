# Integrando-el-funcionamiento-ITBANK
Este repositorio es una propuesta por la escuela de innovación del ITBA en el SPRINT 7 y 8 de su curso de desarrollador fullstack.
El objetivo es unir el front-end con el back-end.


## Table of contents
  - [Requerimientos especificos](#requerimientos-especificos)
    - [Sprint 7](#sprint-7)
        - Problematica 1
        - Problematica 2
        - Problematica 3
    - [Sprint 8](#sprint-7)
        - Problematica 1
  - [Ejecucion](#ejecucion)
    - [Descargar las dependencias](#descargar-las-dependencias)
    - [Algunas consideraciones si se quiere trabajar sobre un entorno virtual](#algunas-consideraciones-si-se-quiere-trabajar-sobre-un-entorno-virtual)
    - [Levantar el servidor](#levantar-el-servidor)
  - [Funcionamiento](#funcionamiento)
  
  - [Aclaraciones y acotaciones](#aclaraciones-y-acotaciones)
    - [Solucion de errores](#solucion-de-errores)
  - [Links](#links)
  - [Autores](#autores)

## Requerimientos especificos

### Sprint 7
#### Primer problematica
Se requiere crear el proyecto DJANGO homebanking, el mismo estará compuesto por las siguientes apps:
    - Clientes
    - Cuentas
    - Tarjetas
    - Prestamos
    - Login
Se trabajara sobre la Base de datos desarrollada en el sprint 6
Adaptar los templates generados en el frontend dentro de django agregando los `templates tags` necesarios para su utilización. Se deben incluir los `recursos estáticos` utilizados en el diseño del sitio.
Crear las `vistas` que interactúen con los `templates` y el `modelo`

#### Segunda problematica
Incorporar el `registro` y `autenticación de clientes` para todo el sitio. Se debe utilizar el sistema de autenticación provisto por DJANGO.
Se necesita generar una relación entre el usuario que se autentica y la información de cliente almacenada. Debería haber una relación `1 a 1` entre cliente y usuario.
Se debe agregar al menú del home banking la opción de salir o cerrar sesión.
Una vez autenticado el usuario, el home banking debe mostrar su nombre en algún lugar del sitio.
Todas las páginas del sitio tienen que chequear que el usuario esta autenticado.

#### Tercer Problematica
Crear un formulario de solicitud de `préstamos pre-aprobados` dentro del homebanking. El formulario deberá ser enviado por `POST` y tener protección contra `Cross site request forgery`.
Entendiendo que el cliente se autentico en el sitio, podemos obtener los datos de cliente para hacer validaciones.
El cliente debe poder elegir el `tipo de préstamo` y la `fecha de inicio`. El monto de pre aprobación depende del tipo de cliente con los siguientes límites: `BLACK 500000$`, `GOLD 300000$` y `CLASSIC 100000$`
Una vez solicitado debe registrarse en la base de datos la solicitud, impactando en préstamo y en el saldo de cuenta.
En todo momento el formulario informará si la solicitud fue aprobada o rechazada


### Sprint 8
En ITBANK se piensa en facilitar en todo momento la operación de nuestros clientes, por ese motivo, se necesita contar con una API REST que contenga una serie de servicios que permita interactuar con el banco de forma autónoma para nuestros clientes.

La API que vamos a desarrollar es privada, accesible sólo a usuarios registrados e identificados por el banco. En este caso usaremos, Basic Authentication para generar una clave que permita al usuario interactuar con nuestros servicios. Solo un usuario cliente puede consultar sus propios datos
Los servicios a generar que puedan ser utilizados por los clientes son los siguientes:

Los servicios a generar que puedan ser utilizados por los clientes son los
siguientes:
    - OBTENER DATOS DE UN CLIENTE
        Un `cliente` autenticado puede consultar sus propios datos
    - OBTENER SALDO DE CUENTA DE UN CLIENTE
        Un `cliente` autenticado puede obtener el tipo de cuenta y su saldo
    - OBTENER MONTO DE PRESTAMOS DE UN CLIENTE
        Un `cliente` autenticado puede obtener el tipo de préstamo y total del mismo
    - OBTENER MONTO DE PRESTAMOS DE UNA SUCURSAL
        Un `empleado` autenticado puede obtener el listado de préstamos otorgados de una sucursal determinada.
    - OBTENER TARJETAS ASOCIADAS A UN CLIENTE
        Un `empleado` autenticado puede obtener el listado de tarjetas de crédito de un cliente determinado
    - GENERAR UNA SOLICITUD DE PRESTAMO PARA UN CLIENTE
        Un `empleado` autenticado puede solicitar un préstamo para un cliente, registrado el mismo y acreditando el saldo en su cuenta
    - ANULAR SOLICITUD DE PRESTAMO DE CLIENTE
        Un `empleado` autenticado puede anular un préstamo para un cliente, revirtiendo el monto correspondiente
    - MODIFICAR DIRECCION DE UN CLIENTE
        El propio `cliente` autenticado o un `empleado` puede modificar las direcciones.
    - LISTADO DE TODAS LAS SUCURSALES
        Un `endpoint` público que devuelve el listado todas las sucursales con la información correspondiente.

## Ejecucion
Se recomienda estar en un entorno virtual previo a los proximos pasos

### Descargar las dependencias
Debe ejecutarse desde la terminal cmd. Sobre el directorio inicial del repo, en el mismo se encuentra el archivo `requirements.txt`.

    ```
    pip install -r requirements.txt
    ```

### Algunas consideraciones si se quiere trabajar sobre un entorno virtual
Tener en cuenta que de tener problemas con el paquete pip y su no reconocimiento es posible que las variables de entorno de python no se encuentren en el path de sus sistema operativo.

    ``` Desde la terminal cmd
    pip install virtualenvwrapper (Descarga la libreria en la computadora)

    mkvirtualenv ``Nombre del entorno`` (crea el entorno en una carpeta llamada envs en el directorio desde el que se ejecute el comando)

    workon ``Nombre del entorno creado`` (activa el entorno)

    pip install ``dependencia``

    pip list (Muestra todas las dependecias especificas del entorno)

    pip freeze -> requirements.txt (Crea un txt que se puede llamar de cualquier forma pero es una convencion usar "requirements", este txt contiene la informacion de todas las dependencias del entorno virtual. Este  txt sera posteriormente leido por los contribuidores del proyecto para instalar las dependencias, al igual que por el runner del server)

    deactivate (Desactiva el entorno)
    ```

### Levantar el servidor

    ``` Desde la terminal cmd
    manage.py runserver
    ```

## Funcionamiento
A la hora de crear un usuario en un homebanking es necesario que la persona sea `Cliente` del banco y abra su cuenta presencialmente.
Para facilitar este proceso se desarrollo una serie de formularios que se presentan al intentar crear un usuario del homebanking pero no disponer de un `DNI` valido por no ser un cliente actual.
Estos formularios generan un `registro` que contiene datos de cliente, direccion y cuenta. Se debe tener en cuenta que que solo se impactan los datos una vez que los 3 formularios son validados, con la intencion de no quedar con formularios incompletos.
Para este proceso se recurre a almacenar la informacion del interesado en la `session` en cuestion y una vez que se impactan los datos en la Base de Datos `BD` se eliminan de la session.

El formulario de registro de usuarios parte de una query al modelo de clientes para verificar que el cliente exista. Cumplido este proceso aprueba la contraseña y la clave popuestas por el usuario y se guardan los datos en el modelo de usuarios. 
Fue necesario expandir el modelo de usuarios para agregar campos tales como `telefono` o bien `claves foraneas` como el `cliente` asociado. Para lo mismo se tuvo que profundizar en la `custmizacion` del `modelo`, el `manager` y el `admin` predefinidos por django.

Una vez registrado, el cliente es redireccionado al Log In que cuenta con un enlace para restablecer su contraseña de ser requerido, a modo conceptual es resuelto correctamente pero se tuvo que recurrir a que el link que deberia ser enviado por mail sea visualizo desde la terminal dado que no esta resulto el envio de mails desde el servidor.

Una vez logueado, el homebanking cuenta con un boton habilitado para solicitar prestamos, el mismo redirecciona a un formulario que no solo genera el registro en el modelo de prestamos sino que a su vez impacta en el monto de la cuenta del Cliente.

Todos los formularios cuentan con proteccion `csfr`. Al mismo tiempo las vistas del homebanking como `Inicio` y `Prestamos` cuentan con el requerimiento de autencicacion para usuario para poder visualizarlas. Finalmente se dispone de un boton de salir `Log Out` para cerrar la sesion del usuario.





  
## Aclaraciones y acotaciones

### Solucion de errores

#### Importante, suele pasar con foreignkey, 
Si se rompen las migraciones y tira que hay una columna con nombre duplicado ejecutar:
```py
manage.py migrate sites --fake          
#sites es la app que se rompio
```
rejecutar las migraciones


manage.py migrate Prestamos --fake          




#### Consultas a la db

Para guardar información relacionada a tus usuarios, es posible usar un modelo tipo perfil.

```py
from django.contrib.auth.models import User
from django.db import models
class Perfil(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    es_astronauta = models.BooleanField(default=False)
```

Luego, es posible acceder al perfil del usuario como si accedieras a cualquier otro modelo relacionado:
```py
>>> usuario = User.objects.get(username='admin')
>>> usuario.pk
1
>>> usuario.perfil.es_astronauta
False
```



#### ValueError: The field admin.LogEntry.user was declared with a lazy reference to 'Login.usuariocustom', but app 'Login' isn't installed.

It happens if you ran default auth app migrations and later changed the AUTH_USER_MODEL in settings.py. You can try following:

```py
#comments AUTH_USER_MODEL in the settings.py file so it points to a default User Model

Python manage.py migrate auth zero

#Uncomment AUTH_USER_MODEL='recommend.AuthUser'

Python manage.py migrate auth
Source

If it's doesn't solve your problems and you are using Sqlite3 you can:

Delete all migration files except __init__.py file.
```


#### Links utiles frente a diversos errores por no haber customizado el modelo de usuario desde el principio
https://docs.djangoproject.com/en/4.1/topics/auth/customizing/#extending-user
https://coffeebytes.dev/como-personalizar-el-modelo-user-en-django/
https://docs.djangoproject.com/en/4.1/topics/db/models/
https://docs.djangoproject.com/en/4.1/topics/auth/customizing/
https://es.stackoverflow.com/questions/380135/django-inconsistentmigrationhistory-admin-0001-initial-is-applied-before-its
https://stackoverflow.com/questions/44651760/django-db-migrations-exceptions-inconsistentmigrationhistory
https://stackoverflow.com/questions/72562887/django-valueerror-field-admin-logentry-user-was-declared-with-a-lazy-reference
https://es.stackoverflow.com/questions/930/roles-de-usuarios-en-django
https://es.stackoverflow.com/questions/1072/heredando-de-abstractuser-django-admin-no-hashea-passwords-useradmin-no-mues


#### django validators
https://docs.djangoproject.com/en/dev/ref/validators/#regexvalidator


#### asignar valores a una instancia de un modelo partiendo de claves dinamicas, como un iterador
https://stackoverflow.com/questions/18759476/how-to-assign-items-inside-a-model-object-with-django


Se puede llamar al usuario en una view sin necesidad de un formulario si simplemente esta autotenticado en la pagina en cuestion, se recurre al atributo request.user que contiene el usuario activo.

## Links del proyecto
- Solution URL: (https://github.com/EliasUpstein/Integrando-el-funcionamiento)

## Autores
#### Korzusehec, Nicolás
- GitHub - [@NicolasKorzusehec](https://github.com/NicolasKorzusehec)
- LinkedIn - [Nicolás Korzusehec](https://www.linkedin.com/in/nicol%C3%A1s-korzusehec/)

#### Upstein, Elias Román
- GitHub - [@EliasUpstein](https://github.com/EliasUpstein)
- LinkedIn - [/]()

#### Molinas, Nicolás 
- GitHub - [@NicolasGabM](https://github.com/NicolasGabM)
- LinkedIn - [Nicolas Gabriel Molinas](https://www.linkedin.com/in/nicolas-gabriel-molinas-20802a216/)

