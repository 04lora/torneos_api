import bcrypt
from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from app.repositories import usuario_repository
from app.schemas.usuario_schema import UsuarioCreate, UsuarioUpdate


def _hashear_password(password: str) -> str:
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(password.encode("utf-8"), salt).decode("utf-8")


def crear_usuario(db: Session, data: UsuarioCreate):
    if usuario_repository.buscar_por_correo(db, data.correo):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="El correo electrónico ya está registrado.",
        )
    hash_pw = _hashear_password(data.password)
    return usuario_repository.crear(db, data.nombre, data.correo, hash_pw)


def listar_usuarios(db: Session):
    return usuario_repository.listar_todos(db)


def obtener_usuario(db: Session, usuario_id: int):
    usuario = usuario_repository.buscar_por_id(db, usuario_id)
    if not usuario:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Usuario no encontrado.",
        )
    return usuario


def actualizar_usuario(db: Session, usuario_id: int, data: UsuarioUpdate):
    usuario = obtener_usuario(db, usuario_id)

    existente = usuario_repository.buscar_por_correo(db, data.correo)
    if existente and existente.id != usuario_id:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="El correo electrónico ya pertenece a otro usuario.",
        )

    nuevo_hash = _hashear_password(data.password) if data.password else None
    return usuario_repository.actualizar(db, usuario, data.nombre, data.correo, nuevo_hash)


def eliminar_usuario(db: Session, usuario_id: int):
    usuario = obtener_usuario(db, usuario_id)
    usuario_repository.eliminar(db, usuario)
    return {"mensaje": "Usuario eliminado correctamente"}