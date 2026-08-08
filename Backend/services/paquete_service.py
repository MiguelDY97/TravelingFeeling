from fastapi import HTTPException
import repositories.paquete_repository as paquete_repository

def obtener_paquetes():

    try:

        return paquete_repository.obtener_paquetes()

    except Exception as e:

        print(f"Error: {e}")

        raise HTTPException(status_code=500, detail="Ocurrió un error al obtener los paquetes.")

def obtener_paquete_por_id(id: int):

    try:

        paquete = paquete_repository.obtener_paquete_por_id(id)

        if paquete is None:

            raise HTTPException(
                status_code=404,
                detail="Paquete no encontrado"
            )

        return paquete

    except HTTPException:
        raise

    except Exception as e:

        print(f"Error: {e}")

        raise HTTPException(
            status_code=500,
            detail="Error al obtener el paquete."
        )

def crear_paquete(paquete):

    try:

        nuevo_id = paquete_repository.crear_paquete(paquete)

        return {
            "mensaje": "Paquete creado correctamente",
            "id": nuevo_id
        }

    except Exception as e:

        print(f"Error: {e}")

        raise HTTPException(
            status_code=500,
            detail="Error al crear el paquete."
        )

def actualizar_paquete(id: int, paquete):

    try:

        filas_actualizadas = paquete_repository.actualizar_paquete(id, paquete)

        if filas_actualizadas == 0:

            raise HTTPException(
                status_code=404,
                detail="Paquete no encontrado"
            )

        return {
            "mensaje": "Paquete actualizado correctamente"
        }

    except HTTPException:
        raise

    except Exception as e:

        print(f"Error: {e}")

        raise HTTPException(
            status_code=500,
            detail="Error al actualizar el paquete."
        )

def eliminar_paquete(id: int):

    try:

        filas_eliminadas = paquete_repository.eliminar_paquete(id)

        if filas_eliminadas == 0:

            raise HTTPException(status_code=404, detail="Paquete no encontrado")

        return {
            "mensaje": "Paquete eliminado correctamente"
        }

    except HTTPException:
        raise

    except Exception as e:

        print(f"Error: {e}")

        raise HTTPException(status_code=500, detail="Error al eliminar el paquete.")