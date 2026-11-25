from pydantic import BaseModel, Field

class UsuarioBase(BaseModel):
    nombre: str = Field(..., min_length=2, max_length=120, example="Jhon Lora")
    correo: str = Field(..., min_length=5, max_length=150, example="jhonlora232@gmail.com")

class UsuarioCreate(UsuarioBase):
    password: str = Field(..., min_length=6, max_length=100, example="123456")

class UsuarioUpdate(UsuarioBase):
    password: str | None = Field(default=None, min_length=6, max_length=100, example="nuevaClave123")

class UsuarioResponse(UsuarioBase):
    id: int

    class Config:
        from_attributes = True