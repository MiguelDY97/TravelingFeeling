from pydantic import BaseModel
from datetime import date

class Reserva(BaseModel):
    id_usuario: int
    id_destino: int
    fecha_reserva: date
    cantidad_personas: int
    estado: str