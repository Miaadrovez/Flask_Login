# Flask User Management System (Sistema de gestión de usuarios de Flask)

Este es un sistema básico de **Login y Gestión de Usuarios** desarrollado con **Flask** y **PostgreSQL**, diseñado para demostrar funcionalidades básicas de una API REST integrada con un frontend dinámico.

## Características

- **Creación de Usuarios**:
  - Los usuarios pueden registrarse proporcionando un nombre de usuario, correo electrónico y contraseña.
  - La contraseña se encripta utilizando **Fernet** antes de ser almacenada en la base de datos para mayor seguridad.

- **Gestión de Usuarios**:
  - Permite listar todos los usuarios registrados.
  - Incluye funcionalidades para editar y eliminar usuarios específicos.

- **Backend con PostgreSQL**:
  - Los datos de los usuarios se almacenan en una base de datos **PostgreSQL**.
  - La API interactúa con la base de datos utilizando la librería **psycopg2**.

- **Frontend Dinámico**:
  - El frontend utiliza **JavaScript** para interactuar con la API mediante solicitudes **GET**, **POST**, **PUT** y **DELETE**.
  - Proporciona una interfaz amigable para mostrar, agregar, editar y eliminar usuarios en tiempo real.

- **Respuestas en JSON**:
  - Las respuestas del backend están estructuradas en formato **JSON**, lo que facilita la comunicación y el manejo de datos en el frontend.

## Requisitos

- Python 3.8 o superior
- PostgreSQL
- Librerías Python necesarias (especificadas en `requirements.txt`)


