from fastapi import FastAPI
from .database import Base, engine
from .routers import auth as auth_router, studios, modelos, tokens

# Database tables are created during container start via init_db.py

app = FastAPI(title="Studio Tokens API")

app.include_router(auth_router.router)
app.include_router(studios.router)
app.include_router(modelos.router)
app.include_router(tokens.router)
