from pydantic import BaseModel, Field

class Alojamiento(BaseModel):
    nombre: str = Field(min_length=2, max_length=100)
    descripcion: str = Field(min_length=10)
    ciudad: str = Field(min_length=2, max_length=150)
    precio: float = Field(gt=0)
    capacidad_personas: int = Field(gt=0)
    cupos_disponibles: int = Field(ge=0)
    imagen: str