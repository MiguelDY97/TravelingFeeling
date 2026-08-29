from pydantic import BaseModel, Field, field_validator
from datetime import date
from typing import Literal, Optional

class Reserva(BaseModel):
    id_usuario: int = Field(gt=0)
    id_destino: int = Field(gt=0)
    id_paquete: Optional[int] = Field(default=None, gt=0)
    fecha_reserva: date
    cantidad_personas: int = Field(gt=0)
    estado: Literal["pendiente", "confirmada", "cancelada"]

    @field_validator("fecha_reserva")
    @classmethod
    def fecha_no_puede_ser_pasada(cls, valor: date) -> date:

        if valor < date.today():
            raise ValueError("La fecha de reserva no puede ser anterior a hoy")

        return valor