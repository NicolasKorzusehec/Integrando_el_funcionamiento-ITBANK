# Ejecución para levantar el proyecto desde un Codespace de GitHub (Válido para programar desde una tablet)
Antes de comenzar, asegúrate de tener un Codespace configurado para este repositorio. Puedes inicializar un Codespace directamente desde la pestaña "Codespaces" de tu repositorio en GitHub. Una vez que el Codespace esté activo, accede a la consola bash para ejecutar los comandos necesarios.

## Descargar Dependencias

1. Accede desde la consola bash a la carpeta que inicializa el proyecto:

    ```bash
    # Ver los directorios y archivos en la ubicación actual
    ls -a

    # Entrar al directorio de instalación de dependencias
    cd /workspace/Integrando_el_funcionamiento-ITBANK

    # Descargar dependencias utilizando el siguiente comando
    python -m pip install -r homebanking/requirements.txt

    # Volver a la carpeta principal
    cd homebanking
    ```

    **Ubicación para Descargar Dependencias:** `/workspace/Integrando_el_funcionamiento-ITBANK`

    **Ubicación del Proyecto:** `/workspace/Integrando_el_funcionamiento-ITBANK/homebanking`

## Ejecutar el Servidor Django

2. Ejecuta el servidor:

    ```bash
    python manage.py runserver
    ```

    - Puede aparecer un error relacionado con las migraciones. Para solucionarlo, ejecuta los siguientes comandos:

        ```bash
        python manage.py makemigrations
        python manage.py migrate
        ```

    - Repite estos comandos si es necesario. Una vez que se solucionaron las migraciones, vuelve a ejecutar el servidor.

3. Detener el programa: `Ctrl + C`

## Crear Usuario Administrador

4. Ejecuta el siguiente comando para crear un superusuario:

    ```bash
    python manage.py createsuperuser
    ```

5. Ingresa a la pestaña de administración:

    Al final de la URL de la aplicación una vez que se ha iniciado, agrega `/admin`.

6. Completa la información del superusuario:

    - **Superusuario Propuesto:**
        - **Nombre:** ITBA
        - **Correo:** nkorzusehec@gmail.com
        - **Contraseña:** 1234
        - **Clave:** 123



## Problema con la verifiacion CSRF, con el debug false se soluciona pero no puedo correr la app.
Tiene que ver con la url del codespace

Posible solucion:
Add this line to your settings.py. This was not required when I was using 3.2 and now I can't POST a form containing a CSRF without it.

Review this line for any changes needed, for example if you need to swap out https for http.

Root cause is the addition of origin header checking in 4.0.

https://docs.djangoproject.com/en/4.0/ref/settings/#csrf-trusted-origins

