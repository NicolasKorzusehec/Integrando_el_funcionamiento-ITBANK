# Integrando-el-funcionamiento
Espacio de entrega Sprint 7 - Programa Full Stack Developer.

Se creo un usuario basico para ejecucion, valido tanto para unicamente para el login
Nombre de usuario: "usuario"
Contraseña: "1234"

Para solicitar la autenticacion de usuario en cada vista se coloca el decorador @login_required  inmediatamente arriba de la definicion de la view que requiera esa autenticacion

La template de logout no es necesaria.

https://stackoverflow.com/questions/18231057/django-rss-feedparser-returns-a-feed-with-no-title
https://zerotobyte.com/complete-guide-to-django-foreignkey/


Si se rompen las migraciones y tira que hay una columna con nombre duplicado ejecutar:
manage.py migrate sites --fake, sites es la app que se rompio
rejecutar las migraciones