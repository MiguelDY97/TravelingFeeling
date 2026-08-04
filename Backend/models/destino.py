from pydantic import BaseModel

class Destino(BaseModel):

    nombre: str
    descripcion: str
    ciudad: str
    pais: str
    precio: float
    cupos_disponibles: int
    imagen: str