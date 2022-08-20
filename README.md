# Integrando-el-funcionamiento
Espacio de entrega Sprint 7 - Programa Full Stack Developer.

Se creo un usuario basico para ejecucion, valido tanto para unicamente para el login
Nombre de usuario: "usuario"
Contraseña: "1234"

Para solicitar la autenticacion de usuario en cada vista se coloca el decorador @login_required  inmediatamente arriba de la definicion de la view que requiera esa autenticacion

La template de logout no es necesaria.

https://stackoverflow.com/questions/18231057/django-rss-feedparser-returns-a-feed-with-no-title
https://zerotobyte.com/complete-guide-to-django-foreignkey/



# Importante, suele pasar con foreignkey, 
Si se rompen las migraciones y tira que hay una columna con nombre duplicado ejecutar:
```py
manage.py migrate sites --fake          
#sites es la app que se rompio
```
rejecutar las migraciones


manage.py migrate Clientes --fake          




# Consultas a la db

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



# ValueError: The field admin.LogEntry.user was declared with a lazy reference to 'Login.usuariocustom', but app 'Login' isn't installed.

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


# Links utiles frente a diversos errores por no haber customizado el modelo de usuario desde el principio
https://docs.djangoproject.com/en/4.1/topics/auth/customizing/#extending-user
https://coffeebytes.dev/como-personalizar-el-modelo-user-en-django/
https://docs.djangoproject.com/en/4.1/topics/db/models/
https://docs.djangoproject.com/en/4.1/topics/auth/customizing/
https://es.stackoverflow.com/questions/380135/django-inconsistentmigrationhistory-admin-0001-initial-is-applied-before-its
https://stackoverflow.com/questions/44651760/django-db-migrations-exceptions-inconsistentmigrationhistory
https://stackoverflow.com/questions/72562887/django-valueerror-field-admin-logentry-user-was-declared-with-a-lazy-reference
https://es.stackoverflow.com/questions/930/roles-de-usuarios-en-django
https://es.stackoverflow.com/questions/1072/heredando-de-abstractuser-django-admin-no-hashea-passwords-useradmin-no-mues


django validators
https://docs.djangoproject.com/en/dev/ref/validators/#regexvalidator


# asignar valores a una instancia de un modelo partiendo de claves dinamicas, como un iterador
https://stackoverflow.com/questions/18759476/how-to-assign-items-inside-a-model-object-with-django