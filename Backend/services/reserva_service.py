from fastapi import HTTPException
import repositories.reserva_repository as reserva_repository

def obtener_reservas():

    try:

        return reserva_repository.obtener_reservas()

    except Exception as e:

        print(f"Error: {e}")

        raise HTTPException(status_code=500, detail="Ocurrió un error al obtener las reservas.")

def obtener_reserva_por_id(id: int):

    try:

        reserva = reserva_repository.obtener_reserva_por_id(id)

        if reserva is None:

            raise HTTPException(
                status_code=404,
                detail="Reserva no encontrada"
            )

        return reserva

    except HTTPException:
        raise

    except Exception as e:

        print(f"Error: {e}")

        raise HTTPException(
            status_code=500,
            detail="Error al obtener la reserva."
        )

def crear_reserva(reserva):

    try:

        nuevo_id = reserva_repository.crear_reserva(reserva)

        return {
            "mensaje": "Reserva creada correctamente",
            "id": nuevo_id
        }

    except Exception as e:

        print(f"Error: {e}")

        raise HTTPException(
            status_code=500,
            detail="Error al crear la reserva."
        )

def actualizar_reserva(id: int, reserva):

    try:

        filas_actualizadas = reserva_repository.actualizar_reserva(id, reserva)

        if filas_actualizadas == 0:

            raise HTTPException(
                status_code=404,
                detail="Reserva no encontrada"
            )

        return {
            "mensaje": "Reserva actualizada correctamente"
        }

    except HTTPException:
        raise

    except Exception as e:

        print(f"Error: {e}")

        raise HTTPException(
            status_code=500,
            detail="Error al actualizar la reserva."
        )

def eliminar_reserva(id: int):

    try:

        filas_eliminadas = reserva_repository.eliminar_reserva(id)

        if filas_eliminadas == 0:

            raise HTTPException(status_code=404, detail="Reserva no encontrada")

        return {
            "mensaje": "Reserva eliminada correctamente"
        }

    except HTTPException:
        raise

    except Exception as e:

        print(f"Error: {e}")

        raise HTTPException(status_code=500, detail="Error al eliminar la reserva.")