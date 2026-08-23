from pydantic import BaseModel, Field

class Paquete(BaseModel):
    id_destino: int = Field(gt=0)
    nombre: str = Field(min_length=2, max_length=100)
    descripcion: str = Field(min_length=10)
    duracion_dias: int = Field(gt=0)
    precio: float = Field(gt=0)
    cupos_disponibles: int = Field(ge=0)
    imagen: str