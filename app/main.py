from fastapi import FastAPI
from app.database.conexion import engine, Base
from app.routes import usuarios, torneos

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="API Torneos Deportivos y Usuarios",
    description="FastAPI + PostgreSQL en Neon + Arquitectura por capas",
    version="1.0.0"
)

app.include_router(usuarios.router)
app.include_router(torneos.router)