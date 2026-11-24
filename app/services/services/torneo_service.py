from fastapi import HTTPException
from sqlalchemy.orm import Session
from app.repositories import torneo_repository
from app.schemas.torneo_schema import TorneoCreate, TorneoUpdate

def crear_torneo(db: Session, data: TorneoCreate):
    if data.fecha_finalizacion < data.fecha_inicio:
        raise HTTPException(status_code=400, detail="La fecha final no puede ser menor a la inicial")
    return torneo_repository.crear(db, data)

def obtener_torneos(db: Session, disciplina: str | None = None):
    if disciplina:
        return torneo_repository.filtrar_disciplina(db, disciplina)
    return torneo_repository.listar_todos(db)

def obtener_torneo_id(db: Session, torneo_id: int):
    obj = torneo_repository.buscar_id(db, torneo_id)
    if not obj:
        raise HTTPException(status_code=404, detail="Torneo no encontrado")
    return obj

def editar_torneo(db: Session, torneo_id: int, data: TorneoUpdate):
    if data.fecha_finalizacion < data.fecha_inicio:
        raise HTTPException(status_code=400, detail="La fecha final no puede ser menor a la inicial")
    obj = obtener_torneo_id(db, torneo_id)
    return torneo_repository.actualizar(db, obj, data)

def borrar_torneo(db: Session, torneo_id: int):
    obj = obtener_torneo_id(db, torneo_id)
    torneo_repository.eliminar(db, obj)
    return {"mensaje": "Torneo eliminado"}