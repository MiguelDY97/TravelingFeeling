import bcrypt

def hashear_contraseña(contraseña: str) -> str:

    contraseña_bytes = contraseña.encode("utf-8")
    hash_bytes = bcrypt.hashpw(contraseña_bytes, bcrypt.gensalt())

    return hash_bytes.decode("utf-8")

def verificar_contraseña(contraseña: str, hash_guardado: str) -> bool:

    contraseña_bytes = contraseña.encode("utf-8")
    hash_bytes = hash_guardado.encode("utf-8")

    return bcrypt.checkpw(contraseña_bytes, hash_bytes)