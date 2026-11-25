from sqlalchemy.orm import Session
from app.models.usuario import Usuario

def crear(db: Session, nombre: str, correo: str, password_hash: str) -> Usuario:
    usuario = Usuario(nombre=nombre, correo=correo, password_hash=password_hash)
    db.add(usuario)
    db.commit()
    db.refresh(usuario)
    return usuario

def listar_todos(db: Session) -> list[Usuario]:
    return db.query(Usuario).all()

def buscar_por_id(db: Session, usuario_id: int) -> Usuario | None:
    return db.query(Usuario).filter(Usuario.id == usuario_id).first()

def buscar_por_correo(db: Session, correo: str) -> Usuario | None:
    return db.query(Usuario).filter(Usuario.correo == correo).first()

def actualizar(db: Session, usuario: Usuario, nombre: str, correo: str, password_hash: str | None = None) -> Usuario:
    usuario.nombre = nombre
    usuario.correo = correo
    if password_hash:
        usuario.password_hash = password_hash
    db.commit()
    db.refresh(usuario)
    return usuario

def eliminar(db: Session, usuario: Usuario) -> None:
    db.delete(usuario)
    db.commit()