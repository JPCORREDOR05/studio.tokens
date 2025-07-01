from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .database import Base, engine
from .routers import auth as auth_router, studios, modelos, tokens

# Database tables are created during container start via init_db.py

app = FastAPI(title="Studio Tokens API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth_router.router)
app.include_router(studios.router)
app.include_router(modelos.router)
app.include_router(tokens.router)
