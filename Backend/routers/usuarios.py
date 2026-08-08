from fastapi import APIRouter
from models.usuario import Usuario
from database.conexion import obtener_conexion
import services.usuario_service as usuario_service

router = APIRouter(
    prefix="/usuarios",
    tags=["Usuarios"]
)

@router.post("/")
def crear_usuario(usuario: Usuario):

    return usuario_service.crear_usuario(usuario)

@router.get("/")
def listar_usuarios():

    return usuario_service.obtener_usuarios()

@router.get("/{id}")
def obtener_usuario_por_id(id: int):

    return usuario_service.obtener_usuario_por_id(id)

@router.put("/{id}")
def actualizar_usuario(id: int, usuario: Usuario):

    return usuario_service.actualizar_usuario(id, usuario)

@router.delete("/{id}")
def eliminar_usuario(id: int):

    return usuario_service.eliminar_usuario(id)