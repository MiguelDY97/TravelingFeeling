from repositories.reserva_repository import (
    obtener_reservas,
    obtener_reserva_por_id,
    crear_reserva,
    actualizar_reserva,
    eliminar_reserva
)

def listar_reservas():
    return obtener_reservas()

def buscar_reserva_por_id(id):
    return obtener_reserva_por_id(id)

def guardar_reserva(reserva):
    crear_reserva(reserva)

def modificar_reserva(id, reserva):
    return actualizar_reserva(id, reserva)

def borrar_reserva(id):
    return eliminar_reserva(id)