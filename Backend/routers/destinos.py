from fastapi import APIRouter
from models.destino import Destino
import services.destino_service as destino_service

router = APIRouter(
    prefix="/destinos",
    tags=["Destinos"]
)

@router.get("/")
def listar_destinos():

    return destino_service.listar_destinos()

@router.get("/{id}")
def buscar_destino_por_id(id: int):

    return destino_service.buscar_destino_por_id(id)

@router.post("/")
def crear_destino(destino: Destino):

    return destino_service.crear_destino(destino)

@router.put("/{id}")
def actualizar_destino(id: int, destino: Destino):

    return destino_service.actualizar_destino(id, destino)

@router.delete("/{id}")
def eliminar_destino(id: int):

    return destino_service.eliminar_destino(id)

   
