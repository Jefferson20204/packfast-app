# PackFast Inventory Management System

PackFast es una aplicación web diseñada para ayudar a las empresas a organizar su inventario de manera eficiente. Este proyecto utiliza el patrón de diseño MVC (Modelo-Vista-Controlador) y está construido con Flask, un microframework de Python.

## Estructura del Proyecto

El proyecto está organizado de la siguiente manera:

```
packfast-app
├── app
│   ├── __init__.py               # Inicializa la aplicación Flask y configura la base de datos
│   ├── models                     # Contiene los modelos de datos
│   │   ├── __init__.py
│   │   ├── user.py                # Define la clase User para la gestión de usuarios
│   │   └── inventory.py           # Define la clase Inventory para la gestión de productos
│   ├── views                      # Contiene las vistas de la aplicación
│   │   ├── __init__.py
│   │   ├── auth_view.py           # Vistas para autenticación (inicio de sesión y registro)
│   │   ├── user_profile_view.py    # Vista del perfil de usuario
│   │   └── admin_profile_view.py   # Vista del perfil de administrador
│   ├── controllers                # Contiene los controladores de la aplicación
│   │   ├── __init__.py
│   │   ├── auth_controller.py      # Controlador para la lógica de autenticación
│   │   ├── user_controller.py       # Controlador para la lógica del perfil de usuario
│   │   └── admin_controller.py      # Controlador para la gestión de usuarios e inventario
│   ├── templates                  # Plantillas HTML de la aplicación
│   │   ├── base.html              # Plantilla base
│   │   ├── login.html             # Plantilla para la página de inicio de sesión
│   │   ├── register.html          # Plantilla para la página de registro
│   │   ├── user_profile.html       # Plantilla para el perfil de usuario
│   │   └── admin_profile.html      # Plantilla para el perfil de administrador
│   └── static                     # Archivos estáticos (CSS y JS)
│       ├── css
│       │   └── style.css          # Estilos CSS de la aplicación
│       └── js
│           └── main.js            # Código JavaScript de la aplicación
├── config.py                      # Configuración de la aplicación
├── requirements.txt               # Dependencias necesarias para el proyecto
├── README.md                      # Documentación del proyecto
└── run.py                         # Punto de entrada de la aplicación
```

## Funcionalidades

- **Inicio de Sesión**: Los usuarios pueden iniciar sesión en la aplicación para acceder a su perfil.
- **Registro**: Los nuevos usuarios pueden registrarse para crear una cuenta.
- **Perfil de Usuario**: Los usuarios pueden ver y editar su información personal.
- **Perfil de Administrador**: Los administradores pueden gestionar cuentas de usuario y el inventario de productos.

## Requisitos

Para ejecutar este proyecto, asegúrate de tener instaladas las siguientes dependencias:

- Flask
- SQLAlchemy
- Flask-Login
- Otras dependencias especificadas en `requirements.txt`

## Instalación

1. Clona el repositorio.
2. Navega al directorio del proyecto.
3. Instala las dependencias con `pip install -r requirements.txt`.
4. Configura la base de datos en `config.py`.
5. Ejecuta la aplicación con `python run.py`.

## Contribuciones

Las contribuciones son bienvenidas. Si deseas contribuir, por favor abre un issue o envía un pull request.

## Licencia

Este proyecto está bajo la Licencia MIT.