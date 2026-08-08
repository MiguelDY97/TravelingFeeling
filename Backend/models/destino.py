from pydantic import BaseModel

class Destino(BaseModel):
    nombre: str
    descripcion: str
    ciudad: str
    precio: float
    cupos_disponibles: int
    imagen: str