from datetime import date
from pydantic import BaseModel, Field

class TorneoBase(BaseModel):
    nombre_torneo: str = Field(..., min_length=3, max_length=150, example="Copa Medellín")
    disciplina: str = Field(..., min_length=2, max_length=100, example="Fútbol")
    fecha_inicio: date = Field(..., example="2026-12-01")
    fecha_finalizacion: date = Field(..., example="2026-12-10")
    numero_participantes: int = Field(..., gt=1, example=16)

class TorneoCreate(TorneoBase):
    pass

class TorneoUpdate(TorneoBase):
    pass

class TorneoResponse(TorneoBase):
    id: int

    class Config:
        from_attributes = True