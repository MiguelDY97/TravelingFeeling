from fastapi import HTTPException
import repositories.alojamiento_repository as alojamiento_repository

def obtener_alojamientos():

    try:

        return alojamiento_repository.obtener_alojamientos()

    except Exception as e:

        print(f"Error: {e}")

        raise HTTPException(status_code=500, detail="Ocurrió un error al obtener los alojamientos.")

def obtener_alojamiento_por_id(id: int):

    try:

        alojamiento = alojamiento_repository.obtener_alojamiento_por_id(id)

        if alojamiento is None:

            raise HTTPException(
                status_code=404,
                detail="Alojamiento no encontrado"
            )

        return alojamiento

    except HTTPException:
        raise

    except Exception as e:

        print(f"Error: {e}")

        raise HTTPException(
            status_code=500,
            detail="Error al obtener el alojamiento."
        )

def crear_alojamiento(alojamiento):

    try:

        nuevo_id = alojamiento_repository.crear_alojamiento(alojamiento)

        return {
            "mensaje": "Alojamiento creado correctamente",
            "id": nuevo_id
        }

    except Exception as e:

        print(f"Error: {e}")

        raise HTTPException(
            status_code=500,
            detail="Error al crear el alojamiento."
        )

def actualizar_alojamiento(id: int, alojamiento):

    try:

        filas_actualizadas = alojamiento_repository.actualizar_alojamiento(id, alojamiento)

        if filas_actualizadas == 0:

            raise HTTPException(
                status_code=404,
                detail="Alojamiento no encontrado"
            )

        return {
            "mensaje": "Alojamiento actualizado correctamente"
        }

    except HTTPException:
        raise

    except Exception as e:

        print(f"Error: {e}")

        raise HTTPException(
            status_code=500,
            detail="Error al actualizar el alojamiento."
        )

def eliminar_alojamiento(id: int):

    try:

        filas_eliminadas = alojamiento_repository.eliminar_alojamiento(id)

        if filas_eliminadas == 0:

            raise HTTPException(status_code=404, detail="Alojamiento no encontrado")

        return {
            "mensaje": "Alojamiento eliminado correctamente"
        }

    except HTTPException:
        raise

    except Exception as e:

        print(f"Error: {e}")

        raise HTTPException(status_code=500, detail="Error al eliminar el alojamiento.")