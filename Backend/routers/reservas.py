from fastapi import APIRouter, HTTPException
from models.reserva import Reserva
from services.reserva_service import (
    listar_reservas,
    buscar_reserva_por_id,
    guardar_reserva,
    modificar_reserva,
    borrar_reserva
)

router = APIRouter(
    prefix="/reservas",
    tags=["Reservas"]
)

@router.get("/")
def obtener_reservas():
    return listar_reservas()

@router.get("/{id}")
def obtener_reserva(id: int):
    reserva = buscar_reserva_por_id(id)

    if reserva is None:
        raise HTTPException(status_code=404, detail="Reserva no encontrada")

    return reserva

@router.post("/")
def crear_reserva(reserva: Reserva):
    guardar_reserva(reserva)
    return {"mensaje": "Reserva creada correctamente"}

@router.put("/{id}")
def actualizar_reserva(id: int, reserva: Reserva):
    filas = modificar_reserva(id, reserva)

    if filas == 0:
        raise HTTPException(status_code=404, detail="Reserva no encontrada")

    return {"mensaje": "Reserva actualizada correctamente"}

@router.delete("/{id}")
def eliminar_reserva(id: int):
    filas = borrar_reserva(id)

    if filas == 0:
        raise HTTPException(status_code=404, detail="Reserva no encontrada")

    return {"mensaje": "Reserva eliminada correctamente"}