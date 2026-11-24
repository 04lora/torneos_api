from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from app.database.conexion import get_db
from app.schemas.torneo_schema import TorneoCreate, TorneoUpdate, TorneoResponse
from app.services import torneo_service

router = APIRouter(prefix="/torneos", tags=["Torneos"])

@router.post("/", response_model=TorneoResponse, status_code=201)
def crear(data: TorneoCreate, db: Session = Depends(get_db)):
    return torneo_service.crear_torneo(db, data)

@router.get("/", response_model=list[TorneoResponse])
def listar(disciplina: str | None = Query(default=None), db: Session = Depends(get_db)):
    return torneo_service.obtener_torneos(db, disciplina)

@router.get("/{torneo_id}", response_model=TorneoResponse)
def por_id(torneo_id: int, db: Session = Depends(get_db)):
    return torneo_service.obtener_torneo_id(db, torneo_id)

@router.put("/{torneo_id}", response_model=TorneoResponse)
def actualizar(torneo_id: int, data: TorneoUpdate, db: Session = Depends(get_db)):
    return torneo_service.editar_torneo(db, torneo_id, data)

@router.delete("/{torneo_id}")
def eliminar(torneo_id: int, db: Session = Depends(get_db)):
    return torneo_service.borrar_torneo(db, torneo_id)