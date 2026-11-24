from sqlalchemy.orm import Session
from app.models.torneo import Torneo
from app.schemas.torneo_schema import TorneoCreate, TorneoUpdate

def crear(db: Session, data: TorneoCreate) -> Torneo:
    obj = Torneo(**data.model_dump())
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj

def listar_todos(db: Session) -> list[Torneo]:
    return db.query(Torneo).all()

def buscar_id(db: Session, torneo_id: int) -> Torneo | None:
    return db.query(Torneo).filter(Torneo.id == torneo_id).first()

def filtrar_disciplina(db: Session, disciplina: str) -> list[Torneo]:
    return db.query(Torneo).filter(Torneo.disciplina.ilike(f"%{disciplina}%")).all()

def actualizar(db: Session, obj: Torneo, data: TorneoUpdate) -> Torneo:
    for k, v in data.model_dump().items():
        setattr(obj, k, v)
    db.commit()
    db.refresh(obj)
    return obj

def eliminar(db: Session, obj: Torneo) -> None:
    db.delete(obj)
    db.commit()