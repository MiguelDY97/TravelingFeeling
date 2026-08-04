from pydantic import BaseModel

class Usuario(BaseModel):
    nombre: str
    apellido: str
    correo: str
    telefono: str
    contraseña: str