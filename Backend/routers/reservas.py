from fastapi import APIRouter
from models.reserva import Reserva
import services.reserva_service as reserva_service

router = APIRouter(
    prefix="/reservas",
    tags=["Reservas"]
)

@router.post("/")
def crear_reserva(reserva: Reserva):

    return reserva_service.crear_reserva(reserva)

@router.get("/")
def listar_reservas():

    return reserva_service.obtener_reservas()

@router.get("/{id}")
def obtener_reserva_por_id(id: int):

    return reserva_service.obtener_reserva_por_id(id)

@router.put("/{id}")
def actualizar_reserva(id: int, reserva: Reserva):

    return reserva_service.actualizar_reserva(id, reserva)

@router.delete("/{id}")
def eliminar_reserva(id: int):

    return reserva_service.eliminar_reserva(id)