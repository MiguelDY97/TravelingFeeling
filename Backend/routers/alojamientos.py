from fastapi import APIRouter
from models.alojamiento import Alojamiento
import services.alojamiento_service as alojamiento_service

router = APIRouter(
    prefix="/alojamientos",
    tags=["Alojamientos"]
)

@router.post("/")
def crear_alojamiento(alojamiento: Alojamiento):

    return alojamiento_service.crear_alojamiento(alojamiento)

@router.get("/")
def listar_alojamientos():

    return alojamiento_service.obtener_alojamientos()

@router.get("/{id}")
def obtener_alojamiento_por_id(id: int):

    return alojamiento_service.obtener_alojamiento_por_id(id)

@router.put("/{id}")
def actualizar_alojamiento(id: int, alojamiento: Alojamiento):

    return alojamiento_service.actualizar_alojamiento(id, alojamiento)

@router.delete("/{id}")
def eliminar_alojamiento(id: int):

    return alojamiento_service.eliminar_alojamiento(id)