from fastapi import FastAPI
from app.database.conexion import engine, Base
from app.routes import torneos

Base.metadata.create_all(bind=engine)

app = FastAPI(title="API Torneos Deportivos")
app.include_router(torneos.router)