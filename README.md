# Proyecto de Enriquecimiento de Transacciones

![Banner del Proyecto](https://via.placeholder.com/1200x300?text=Enriquecimiento+de+Transacciones) <!-- Reemplaza el enlace con una imagen representativa si tienes una. -->

[![Python](https://img.shields.io/badge/Python-3.9%2B-blue)](https://www.python.org/) [![Django](https://img.shields.io/badge/Django-4.0%2B-green)](https://www.djangoproject.com/) [![PostgreSQL](https://img.shields.io/badge/PostgreSQL-14%2B-blue)](https://www.postgresql.org/) [![Docker](https://img.shields.io/badge/Docker-20.10%2B-blue)](https://www.docker.com/)

Este proyecto es una prueba técnica para enriquecer transacciones bancarias mediante una API REST utilizando **Django** y **PostgreSQL**.

---

## Tabla de Contenidos

1. [Descripción](#1-descripción)
2. [Tecnologías](#2-tecnologías)
3. [Instalación](#3-instalación)
   - [Requisitos Previos](#31-requisitos-previos)
   - [Clonar el Repositorio](#32-clonar-el-repositorio)
   - [Construir y Ejecutar la Aplicación](#33-construir-y-ejecutar-la-aplicación)
   - [Migrar la Base de Datos](#34-migrar-la-base-de-datos)
4. [Uso](#4-uso)
   - [Endpoints Principales](#41-endpoints-principales)
   - [Uso del Admin de Django](#42-uso-del-admin-de-django)
5. [Contribuciones](#5-contribuciones)

---

## 1. Descripción

La API permite enriquecer transacciones bancarias con información sobre categorías, nombres de comercios y logotipos, utilizando un sistema de keywords. Los usuarios pueden enviar un listado de transacciones y recibir datos enriquecidos.

---

## 2. Tecnologías

Este proyecto utiliza las siguientes herramientas y tecnologías:

- **[Django](https://www.djangoproject.com/):** Framework web para Python.
- **[Django REST Framework](https://www.django-rest-framework.org/):** Creación de APIs RESTful.
- **[PostgreSQL](https://www.postgresql.org/):** Sistema de gestión de bases de datos.
- **[Docker](https://www.docker.com/):** Contenerización de la aplicación.
- **[Docker Compose](https://docs.docker.com/compose/):** Orquestación de contenedores.

---

## 3. Instalación

### 3.1 Requisitos Previos

- Tener [Docker](https://www.docker.com/get-started) y [Docker Compose](https://docs.docker.com/compose/) instalados.

### 3.2 Clonar el Repositorio

```bash
git clone https://github.com/eduan-villegas/getxerpa.git
cd getxerpa
```

### 3.3 Construir y Ejecutar la Aplicación

```bash
docker-compose up --build
```

### 3.4 Migrar la Base de Datos

En otro terminal, ejecuta:

```bash
docker-compose exec web python manage.py migrate
```

---

## 4. Uso

### 4.1 Endpoints Principales

#### Transacciones
- **GET** `/api/transacciones/`: Listar todas las transacciones.
- **POST** `/api/transacciones/`: Enviar un listado de transacciones para enriquecer.
- **GET** `/api/transacciones/{id}/`: Obtener detalles de una transacción específica.
- **PUT** `/api/transacciones/{id}/`: Actualizar una transacción específica.
- **DELETE** `/api/transacciones/{id}/`: Eliminar una transacción específica.

#### Categorías
- **GET** `/api/categorias/`: Listar todas las categorías.
- **POST** `/api/categorias/`: Crear una nueva categoría.
- **GET** `/api/categorias/{id}/`: Obtener detalles de una categoría específica.
- **PUT** `/api/categorias/{id}/`: Actualizar una categoría específica.
- **DELETE** `/api/categorias/{id}/`: Eliminar una categoría específica.

### 4.2 Uso del Admin de Django

#### Crear un Superusuario

Para acceder al panel de administración, necesitas crear un superusuario:

```bash
docker-compose exec web python manage.py createsuperuser
```

#### Acceso al Panel de Administración

Accede a: [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/) e inicia sesión con las credenciales del superusuario.

---

## 5. Contribuciones

¡Contribuciones son bienvenidas! Por favor, abre un [issue](https://github.com/eduan-villegas/getxerpa.git/issues) o envía un pull request.