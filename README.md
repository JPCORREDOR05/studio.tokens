# Studio Tokens Platform

Este proyecto provee una API en **FastAPI** junto con un placeholder de frontend en **React**. La base de datos utilizada es **PostgreSQL** y todo el entorno se puede levantar fácilmente con Docker Compose.

## Estructura
- `backend/` – Código de la API (FastAPI) y modelos de base de datos.
- `frontend/` – Código React (placeholder) para futuras interfaces de usuario.

## Requisitos
- [Docker](https://docs.docker.com/get-docker/) y [Docker Compose](https://docs.docker.com/compose/).

## Puesta en marcha rápida
1. Copia el archivo `.env.example` a `.env` en la raíz del proyecto y ajusta las variables si es necesario.
2. Ejecuta:

```bash
docker-compose up --build
```

Esto creará los contenedores de base de datos y backend. La API quedará disponible en `http://localhost:8000`.

## Variables de entorno
El servicio `backend` usa las siguientes variables de entorno:
- `DATABASE_URL` – cadena de conexión a PostgreSQL.
- `JWT_SECRET_KEY` – clave secreta para firmar los tokens JWT.

Puedes modificar estos valores en el archivo `.env` o directamente en `docker-compose.yml`.

## Esquema de la base de datos
El modelo sigue la estructura propuesta con tablas para usuarios, modelos y registros diarios de tokens para Chaturbate y Stripchat.

## Scripts útiles
Durante el desarrollo puedes verificar que el código Python compile correctamente con:

```bash
python -m py_compile backend/app/*.py backend/app/routers/*.py
```

---

Con estos pasos tendrás un entorno listo para realizar pruebas iniciales de la plataforma.
