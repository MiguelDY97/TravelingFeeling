from fastapi import HTTPException
import repositories.usuario_repository as usuario_repository


def obtener_usuarios():

    try:

        return usuario_repository.obtener_usuarios()

    except Exception as e:

        print(f"Error: {e}")

        raise HTTPException(status_code=500, detail="Ocurrió un error al obtener los usuarios.")

def obtener_usuario_por_id(id: int):

    try:

        usuario = usuario_repository.obtener_usuario_por_id(id)

        if usuario is None:

            raise HTTPException(
                status_code=404,
                detail="Usuario no encontrado"
            )

        return usuario

    except HTTPException:
        raise

    except Exception as e:

        print(f"Error: {e}")

        raise HTTPException(
            status_code=500,
            detail="Error al obtener el usuario."
        )
    
def crear_usuario(usuario):

    try:

        nuevo_id = usuario_repository.crear_usuario(usuario)

        return {
            "mensaje": "Usuario creado correctamente",
            "id": nuevo_id
        }

    except Exception as e:

        print(f"Error: {e}")

        raise HTTPException(
            status_code=500,
            detail="Error al crear el usuario."
        )

def actualizar_usuario(id: int, usuario):

    try:

        filas_actualizadas = usuario_repository.actualizar_usuario(id, usuario)

        if filas_actualizadas == 0:

            raise HTTPException(
                status_code=404,
                detail="Usuario no encontrado"
            )

        return {
            "mensaje": "Usuario actualizado correctamente"
        }

    except HTTPException:
        raise

    except Exception as e:

        print(f"Error: {e}")

        raise HTTPException(
            status_code=500,
            detail="Error al actualizar el usuario."
        )
    
def eliminar_usuario(id: int):

    try:

        filas_eliminadas = usuario_repository.eliminar_usuario(id)

        if filas_eliminadas == 0:

            raise HTTPException(status_code=404, detail="Usuario no encontrado")

        return {
            "mensaje": "Usuario eliminado correctamente"
        }

    except HTTPException:
        raise

    except Exception as e:

        print(f"Error: {e}")

        raise HTTPException( status_code=500, detail="Error al eliminar el usuario.")