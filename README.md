# Studio Tokens Platform

Este proyecto provee una API en **FastAPI** y un frontend en **React**. La base de datos utilizada es **PostgreSQL** y todo el entorno se puede levantar fácilmente con Docker Compose.

## Estructura
- `backend/` – Código de la API (FastAPI) y modelos de base de datos.
- `frontend/` – Código React que se sirve en el puerto `3000` al levantar los contenedores.

## Requisitos
- [Docker](https://docs.docker.com/get-docker/) y [Docker Compose](https://docs.docker.com/compose/).
- Python 3.10 si deseas ejecutar sin Docker (requiere las dependencias listadas en `backend/requirements.txt`)

## Puesta en marcha rápida
Ejecuta directamente:

```bash
docker-compose up --build
```

Esto creará los contenedores de base de datos, backend y frontend. Puede tardar unos segundos en estar disponible mientras el backend espera a que la base de datos acepte conexiones.
La API quedará disponible en `http://localhost:8000` y el frontend en `http://localhost:3000`.
Al iniciar por primera vez se generará automáticamente el usuario `juan-pablo` con rol `superadmin`. La contraseña se mostrará en los logs del contenedor `backend`.

## Variables de entorno
El servicio `backend` usa las siguientes variables de entorno:
- `DATABASE_URL` – cadena de conexión a PostgreSQL.
- `JWT_SECRET_KEY` – clave secreta para firmar los tokens JWT.

Estas variables ya vienen definidas en `docker-compose.yml`, por lo que no es necesario crear manualmente un archivo `.env`.

Si ejecutas el backend sin Docker asegúrate de instalar también la librería `python-multipart`, necesaria para procesar los formularios de login con FastAPI.

## Esquema de la base de datos
El modelo sigue la estructura propuesta con tablas para usuarios, modelos y registros diarios de tokens para Chaturbate y Stripchat.

## Scripts útiles
Durante el desarrollo puedes verificar que el código Python compile correctamente con:

```bash
python -m py_compile backend/app/*.py backend/app/routers/*.py
```

---

Con estos pasos tendrás un entorno listo para realizar pruebas iniciales de la plataforma.
