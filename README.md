
# Proyecto Flask con Autenticación y Autorización por Roles

Este proyecto demuestra cómo crear una aplicación Flask que implemente autenticación de usuarios y autorización basada en roles utilizando Flask-Login y Flask-Principal.

## 🛠️ Configuración del Proyecto

1. Clona el repositorio base o usa el código de clase:  
   https://github.com/javierdastas/comp2052

2. Instala las dependencias:
   ```bash
   pip install flask flask-login flask-principal
   ```

3. Ejecuta la aplicación:
   ```bash
   flask run
   ```

## 🔐 Funcionalidades

- Inicio de sesión de usuarios
- Asignación de roles y permisos
- Protección de rutas usando `Flask-Principal`
- Simulación de acceso según rol

## 🧩 Roles y Permisos

Los roles se definen en el back-end. Cada ruta está protegida con permisos específicos.  
Ejemplo de roles:
- **admin**: acceso completo
- **editor**: acceso a edición
- **viewer**: solo lectura

## 🧪 Pruebas de Funcionalidad

Puedes probar las rutas protegidas usando:

- **Postman**
- **REST Client de VSCode**
- Navegador web (para rutas GET)

Asegúrate de autenticarte primero y luego acceder a rutas según el rol del usuario simulado.

## 📂 Estructura del Proyecto

```
/app
│
├── __init__.py
├── routes.py
├── models.py
└── auth.py
```

## 📸 Diagrama de Flujo

Ver el archivo PDF adjunto con el diagrama que explica el flujo de autorización.

## 👨‍💻 Autor

- jvisawesome
- Curso COMP2052
