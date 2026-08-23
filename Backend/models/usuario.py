from pydantic import BaseModel, EmailStr, Field

class Usuario(BaseModel):
    nombre: str = Field(min_length=2, max_length=100)
    apellido: str = Field(min_length=2, max_length=100)
    correo: EmailStr
    telefono: str = Field(pattern=r'^\d{10}$')
    contraseña: str = Field(min_length=8)