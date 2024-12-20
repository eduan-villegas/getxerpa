# Proyecto de Enriquecimiento de Transacciones

Este proyecto es una prueba técnica para enriquecer transacciones bancarias mediante una API REST utilizando Django y PostgreSQL.

## Tabla de Contenidos

1. [Descripción](#descripción)
2. [Tecnologías](#tecnologías)
3. [Instalación](#instalación)
4. [Uso](#uso)
5. [Endpoints](#endpoints)
6. [Uso del Admin de Django](#uso-del-admin-de-django)

## Descripción

La API permite enriquecer transacciones bancarias con información sobre categorías, nombres de comercios y logotipos, utilizando un sistema de keywords. Los usuarios pueden enviar un listado de transacciones y recibir datos enriquecidos.

## Tecnologías

- **Django**: Framework web para Python.
- **Django REST Framework**: Para la creación de APIs RESTful.
- **PostgreSQL**: Sistema de gestión de bases de datos.
- **Docker**: Contenerización de la aplicación.
- **Docker Compose**: Orquestación de contenedores.

## Instalación

### Requisitos Previos

- Tener [Docker](https://www.docker.com/get-started) y [Docker Compose](https://docs.docker.com/compose/) instalados en tu máquina.

### Clonar el Repositorio

git clone <URL_DEL_REPOSITORIO>
cd <NOMBRE_DEL_DIRECTORIO>

### Construir y Ejecutar la Aplicación

docker-compose up --build

### Migrar la Base de Datos
En otro terminal, ejecuta:

docker-compose exec web python manage.py migrate

### Uso
Una vez que la aplicación esté en funcionamiento, puedes acceder a la API en:

http://127.0.0.1:8000/api/

### Endpoints
A continuación se describen los principales endpoints disponibles:

Transacciones
GET /api/transacciones/: Listar todas las transacciones.
POST /api/transacciones/: Enviar un listado de transacciones para enriquecer.
GET /api/transacciones/{id}/: Obtener detalles de una transacción específica.
PUT /api/transacciones/{id}/: Actualizar una transacción específica.
DELETE /api/transacciones/{id}/: Eliminar una transacción específica.

Categorías
GET /api/categorias/: Listar todas las categorías.
POST /api/categorias/: Crear una nueva categoría.
GET /api/categorias/{id}/: Obtener detalles de una categoría específica.
PUT /api/categorias/{id}/: Actualizar una categoría específica.
DELETE /api/categorias/{id}/: Eliminar una categoría específica.

Comercios
GET /api/comercios/: Listar todos los comercios.
POST /api/comercios/: Crear un nuevo comercio.
GET /api/comercios/{id}/: Obtener detalles de un comercio específico.
PUT /api/comercios/{id}/: Actualizar un comercio específico.
DELETE /api/comercios/{id}/: Eliminar un comercio específico.

Keywords
GET /api/keywords/: Listar todas las keywords.
POST /api/keywords/: Crear una nueva keyword.
GET /api/keywords/{id}/: Obtener detalles de una keyword específica.
PUT /api/keywords/{id}/: Actualizar una keyword específica.
DELETE /api/keywords/{id}/: Eliminar una keyword específica.

## Uso del Admin de Django

### Crear un superusuario
Para acceder al panel de administración, necesitas crear un superusuario. Ejecuta el siguiente comando en otra terminal:

docker-compose exec web python manage.py createsuperuser

Se te pedirá que ingreses un nombre de usuario, un correo electrónico y una contraseña. Asegúrate de recordar estas credenciales.

### Acceder al panel de administración
Una vez creado el superusuario, puedes acceder al panel de administración abriendo tu navegador en:

http://127.0.0.1:8000/admin/

Inicia sesión con las credenciales del superusuario que creaste.