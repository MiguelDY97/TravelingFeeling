from fastapi import APIRouter
from models.paquete import Paquete
import services.paquete_service as paquete_service

router = APIRouter(
    prefix="/paquetes",
    tags=["Paquetes"]
)

@router.post("/")
def crear_paquete(paquete: Paquete):

    return paquete_service.crear_paquete(paquete)

@router.get("/")
def listar_paquetes():

    return paquete_service.obtener_paquetes()

@router.get("/{id}")
def obtener_paquete_por_id(id: int):

    return paquete_service.obtener_paquete_por_id(id)

@router.put("/{id}")
def actualizar_paquete(id: int, paquete: Paquete):

    return paquete_service.actualizar_paquete(id, paquete)

@router.delete("/{id}")
def eliminar_paquete(id: int):

    return paquete_service.eliminar_paquete(id)