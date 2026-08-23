from database.conexion import obtener_conexion

def obtener_usuarios():

    conexion = None
    cursor = None

    try:

        conexion = obtener_conexion()
        cursor = conexion.cursor(dictionary=True)

        cursor.execute("SELECT * FROM usuarios")

        return cursor.fetchall()

    finally:

        if cursor:
            cursor.close()

        if conexion:
            conexion.close()

def obtener_usuario_por_id(id: int):

    conexion = None
    cursor = None

    try:

        conexion = obtener_conexion()
        cursor = conexion.cursor(dictionary=True)

        cursor.execute(
            "SELECT * FROM usuarios WHERE id = %s",
            (id,)
        )

        return cursor.fetchone()

    finally:

        if cursor:
            cursor.close()

        if conexion:
            conexion.close()

def obtener_usuario_por_correo(correo: str):

    conexion = None
    cursor = None

    try:

        conexion = obtener_conexion()
        cursor = conexion.cursor(dictionary=True)

        cursor.execute(
            "SELECT * FROM usuarios WHERE correo = %s",
            (correo,)
        )

        return cursor.fetchone()

    finally:

        if cursor:
            cursor.close()

        if conexion:
            conexion.close()

def crear_usuario(usuario):

    conexion = None
    cursor = None

    try:

        conexion = obtener_conexion()
        cursor = conexion.cursor()

        sql = """
        INSERT INTO usuarios
        (nombre, apellido, correo, telefono, contraseña)
        VALUES (%s, %s, %s, %s, %s)
        """

        valores = (
            usuario.nombre,
            usuario.apellido,
            usuario.correo,
            usuario.telefono,
            usuario.contraseña
        )

        cursor.execute(sql, valores)

        conexion.commit()

        return cursor.lastrowid

    finally:

        if cursor:
            cursor.close()

        if conexion:
            conexion.close()

def actualizar_usuario(id: int, usuario):

    conexion = None
    cursor = None

    try:

        conexion = obtener_conexion()
        cursor = conexion.cursor()

        sql = """
        UPDATE usuarios
        SET nombre = %s,
            apellido = %s,
            correo = %s,
            telefono = %s,
            contraseña = %s
        WHERE id = %s
        """

        valores = (
            usuario.nombre,
            usuario.apellido,
            usuario.correo,
            usuario.telefono,
            usuario.contraseña,
            id
        )

        cursor.execute(sql, valores)

        conexion.commit()

        return cursor.rowcount

    finally:

        if cursor:
            cursor.close()

        if conexion:
            conexion.close()

def eliminar_usuario(id: int):

    conexion = None
    cursor = None

    try:

        conexion = obtener_conexion()
        cursor = conexion.cursor()

        cursor.execute(
            "DELETE FROM usuarios WHERE id = %s",
            (id,)
        )

        conexion.commit()

        return cursor.rowcount

    finally:

        if cursor:
            cursor.close()

        if conexion:
            conexion.close()