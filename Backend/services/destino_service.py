from fastapi import HTTPException
import repositories.destino_repository as destino_repository

def listar_destinos():

    try:

        return destino_repository.listar_destinos()

    except Exception as e:

        print(f"Error: {e}")

        raise HTTPException(
            status_code=500,
            detail="Error al obtener los destinos."
        )
    
def buscar_destino_por_id(id: int):

    try:

        destino = destino_repository.buscar_destino_por_id(id)

        if destino is None:

            raise HTTPException(
                status_code=404,
                detail="Destino no encontrado"
            )

        return destino

    except HTTPException:
        raise

    except Exception as e:

        print(f"Error: {e}")

        raise HTTPException(
            status_code=500,
            detail="Error al obtener el destino."
        )
    
def crear_destino(destino):

    try:

        nuevo_id = destino_repository.crear_destino(destino)

        return {
            "mensaje": "Destino creado correctamente",
            "id": nuevo_id
        }

    except Exception as e:

        print(f"Error: {e}")

        raise HTTPException(
            status_code=500,
            detail="Error al crear el destino."
        )
    
def actualizar_destino(id: int, destino):

    try:

        filas_actualizadas = destino_repository.actualizar_destino(id, destino)

        if filas_actualizadas == 0:

            raise HTTPException(
                status_code=404,
                detail="Destino no encontrado"
            )

        return {
            "mensaje": "Destino actualizado correctamente"
        }

    except HTTPException:
        raise

    except Exception as e:

        print(f"Error: {e}")

        raise HTTPException(
            status_code=500,
            detail="Error al actualizar el destino."
        )
    
def eliminar_destino(id: int):

    try:

        filas_eliminadas = destino_repository.eliminar_destino(id)

        if filas_eliminadas == 0:

            raise HTTPException(
                status_code=404,
                detail="Destino no encontrado"
            )

        return {
            "mensaje": "Destino eliminado correctamente"
        }

    except HTTPException:
        raise

    except Exception as e:

        print(f"Error: {e}")

        raise HTTPException(
            status_code=500,
            detail="Error al eliminar el destino."
        )