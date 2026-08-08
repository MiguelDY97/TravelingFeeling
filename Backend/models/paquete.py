from pydantic import BaseModel
 
class Paquete(BaseModel):
 
    id_destino: int
    nombre: str
    descripcion: str
    duracion_dias: int
    precio: float
    cupos_disponibles: int
    imagen: str