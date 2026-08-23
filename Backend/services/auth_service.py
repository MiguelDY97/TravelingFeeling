from fastapi import HTTPException
import repositories.usuario_repository as usuario_repository
from utils.seguridad import verificar_contraseña
from utils.token import crear_token


def login_usuario(login_data):

    try:

        usuario = usuario_repository.obtener_usuario_por_correo(login_data.correo)

        if usuario is None:

            raise HTTPException(
                status_code=401,
                detail="Correo o contraseña incorrectos"
            )

        contraseña_valida = verificar_contraseña(
            login_data.contraseña,
            usuario["contraseña"]
        )

        if not contraseña_valida:

            raise HTTPException(
                status_code=401,
                detail="Correo o contraseña incorrectos"
            )

        token = crear_token({
            "id": usuario["id"],
            "correo": usuario["correo"]
        })

        return {
            "mensaje": "Login exitoso",
            "token": token,
            "usuario": {
                "id": usuario["id"],
                "nombre": usuario["nombre"],
                "apellido": usuario["apellido"],
                "correo": usuario["correo"]
            }
        }

    except HTTPException:
        raise

    except Exception as e:

        print(f"Error: {e}")

        raise HTTPException(
            status_code=500,
            detail="Error al iniciar sesión."
        )