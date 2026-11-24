from sqlalchemy import Column, Integer, String, Date
from app.database.conexion import Base

class Torneo(Base):
    __tablename__ = "torneos"

    id = Column(Integer, primary_key=True, index=True)
    nombre_torneo = Column(String(150), nullable=False)
    disciplina = Column(String(100), nullable=False, index=True)
    fecha_inicio = Column(Date, nullable=False)
    fecha_finalizacion = Column(Date, nullable=False)
    numero_participantes = Column(Integer, nullable=False)