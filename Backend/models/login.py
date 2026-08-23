from pydantic import BaseModel

class LoginRequest(BaseModel):
    correo: str
    contraseña: str