from fastapi import APIRouter,HTTPException
from models.usuario import Usuario
from database.conexion import obtener_conexion
import services.usuario_service as usuario_service

router = APIRouter()

@router.post("/usuarios")
def crear_usuario(usuario: Usuario):

    return usuario_service.crear_usuario(usuario)

@router.get("/usuarios")
def listar_usuarios():

    return usuario_service.obtener_usuarios()

@router.get("/usuarios/{id}")
def obtener_usuario_por_id(id: int):

    return usuario_service.obtener_usuario_por_id(id)

@router.put("/usuarios/{id}")
def actualizar_usuario(id: int, usuario: Usuario):

    return usuario_service.actualizar_usuario(id, usuario)

@router.delete("/usuarios/{id}")
def eliminar_usuario(id: int):

    return usuario_service.eliminar_usuario(id)