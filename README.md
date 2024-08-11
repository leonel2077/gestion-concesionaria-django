# Sistema de Gestión para una Concesionaria de Autos 

## Autores
- [Mariano Leonel Ison](https://github.com/leonel2077)
- [Mateo Roble](https://github.com/MateoRoble)

## Descripción
Este proyecto es un sistema web para la gestión de una concesionaria de autos, desarrollado con Django.

## Instalación y Configuración
1. Clonar el repositorio:
   ```bash
   git clone https://github.com/leonel2077/gestion-concesionaria-django.git
   cd gestion-concesionaria-django
2. Crear y activar un entorno virtual:
   ```bash
   python -m venv venv
   source venv/bin/activate  # En Windows: source venv\Scripts\activate
3. Instalar las dependencias:
   ```bash
   pip install -r requirements.txt
4. Realizar las migraciones iniciales:
   ```bash
   python manage.py migrate
5. Ejecutar el servidor de desarrollo:
   ```bash
   python manage.py runserver

## Funcionalidades

- **Gestión de Autos**: CRUD (Crear, Leer, Actualizar, Eliminar) para los autos.
- **Gestión de Marcas y Modelos**: CRUD para marcas y modelos de autos.
- **Comentarios**: Los usuarios pueden comentar en los detalles de cada auto. Los comentarios pueden ser editados o eliminados solo por el autor del comentario.
- **Roles de Usuario**: Implementación de roles de Administrador y Usuario normal con diferentes permisos.
- **Filtro por Marca**: Filtrado de autos por marca en la lista de autos.

## Estructura del Proyecto

- **Aplicaciones**:
  - `gestion_autos`: Contiene la lógica principal del sistema de gestión de autos.
  - `users`: Gestiona los usuarios y roles.
  - `home`: Contiene las plantillas base, así como las vistas de inicio de sesión y registro.

- **Modelos**:
  - `Auto`: Representa un vehículo en la concesionaria.
  - `Marca`: Define la marca de los autos.
  - `ModeloAuto`: Define el modelo de un auto.
  - `TipoCombustible`: Define el tipo combustible de un auto.
  - `Comentario`: Permite a los usuarios dejar comentarios en los autos.
  - `Pais`: Representa el país de fabricación de los autos.
  - `ImagenAuto`: Representa la imágen del auto.

- **Vistas**:
  - Utiliza vistas basadas en clases (Class-Based Views) para todas las operaciones CRUD.
  - Las vistas para crear, actualizar, y eliminar están restringidas a administradores usando el decorador `user_passes_test`.

- **Context Processors**:
  - `all_marcas`: Proporciona todas las marcas a las plantillas para ser usadas en filtros o dropdowns.
  - `total_autos`: Proporciona la cantidad total de autos registrados en el sistema.
