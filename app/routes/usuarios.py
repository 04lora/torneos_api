from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from app.database.conexion import get_db
from app.schemas.usuario_schema import UsuarioCreate, UsuarioUpdate, UsuarioResponse
from app.services import usuario_service

router = APIRouter(prefix="/usuarios", tags=["Usuarios"])

@router.post("/", response_model=UsuarioResponse, status_code=status.HTTP_201_CREATED)
def crear(data: UsuarioCreate, db: Session = Depends(get_db)):
    return usuario_service.crear_usuario(db, data)

@router.get("/", response_model=list[UsuarioResponse])
def listar(db: Session = Depends(get_db)):
    return usuario_service.listar_usuarios(db)

@router.get("/{usuario_id}", response_model=UsuarioResponse)
def por_id(usuario_id: int, db: Session = Depends(get_db)):
    return usuario_service.obtener_usuario(db, usuario_id)

@router.put("/{usuario_id}", response_model=UsuarioResponse)
def actualizar(usuario_id: int, data: UsuarioUpdate, db: Session = Depends(get_db)):
    return usuario_service.actualizar_usuario(db, usuario_id, data)

@router.delete("/{usuario_id}", status_code=status.HTTP_200_OK)
def eliminar(usuario_id: int, db: Session = Depends(get_db)):
    return usuario_service.eliminar_usuario(db, usuario_id)