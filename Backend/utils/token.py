import jwt
from datetime import datetime, timedelta, timezone

# En un proyecto real esta clave NUNCA va escrita en el codigo,
# se guarda en una variable de entorno (.env). La dejamos aqui
# por simplicidad mientras el proyecto es de aprendizaje.
CLAVE_SECRETA = "cambia_esta_clave_por_una_mas_segura"
ALGORITMO = "HS256"
MINUTOS_EXPIRACION = 60

def crear_token(datos: dict) -> str:
    """
    Genera un token JWT a partir de un diccionario (ej. id y correo
    del usuario). El token incluye una fecha de expiracion.
    """

    datos_token = datos.copy()

    expiracion = datetime.now(timezone.utc) + timedelta(minutes=MINUTOS_EXPIRACION)
    datos_token.update({"exp": expiracion})

    return jwt.encode(datos_token, CLAVE_SECRETA, algorithm=ALGORITMO)

def verificar_token(token: str):
    """
    Decodifica un token y devuelve sus datos si es valido.
    Si el token expiro o fue alterado, devuelve None.
    """

    try:

        return jwt.decode(token, CLAVE_SECRETA, algorithms=[ALGORITMO])

    except jwt.PyJWTError:

        return None