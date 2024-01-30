# Ejecución para levantar el proyecto desde un Codespace de GitHub (Válido para programar desde una tablet)

Antes de comenzar, asegúrate de tener un Codespace configurado para este repositorio. Puedes seguir estos pasos para inicializar un Codespace:

1. Accede al repositorio de tu proyecto en GitHub.

2. Haz clic en el botón "Code" (Código) en la parte superior derecha del repositorio.

3. En lugar de descargar el repositorio, selecciona la pestaña "Codespaces".

4. Haz clic en "New Codespace" para crear un nuevo entorno de desarrollo.

5. Espera a que se configure el entorno. Una vez que el Codespace esté activo, estarás listo para ejecutar los comandos necesarios.

**Nota:** Este proyecto incluye un archivo de configuración `devcontainer.json` que automatiza la configuración del entorno de desarrollo. Al iniciar el Codespace, el entorno se configura automáticamente con las dependencias y configuraciones necesarias.

### Ventajas de Utilizar el Devcontainer

El uso de un archivo `devcontainer.json` preconfigurado ofrece varias ventajas:

- **Configuración Automática:** El entorno de desarrollo se configura automáticamente, eliminando la necesidad de configuraciones manuales.

- **Reproducibilidad:** Todos los desarrolladores trabajan en un entorno consistente y reproducible, reduciendo posibles problemas de configuración.

- **Aislamiento:** El entorno se aísla del sistema operativo del desarrollador, evitando conflictos con otras dependencias locales.

- **Agilidad:** Iniciar un Codespace es rápido y sencillo, lo que mejora la eficiencia y la agilidad en el desarrollo.

Estas ventajas hacen que la configuración del entorno de desarrollo sea más fluida y proporciona una experiencia consistente para todo el equipo de desarrollo.


## Acceso a la Consola Bash

Para acceder a la consola bash en tu Codespace:

1. Busca y selecciona la opción "Open new terminal" (Abrir nueva terminal) en la barra inferior del entorno de Codespace.

2. Se abrirá una consola bash lista para que puedas ejecutar los comandos necesarios para tu proyecto.


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

