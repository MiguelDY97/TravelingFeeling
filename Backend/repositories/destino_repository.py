from database.conexion import obtener_conexion

def listar_destinos():

    conexion = None
    cursor = None

    try:

        conexion = obtener_conexion()
        cursor = conexion.cursor(dictionary=True)

        cursor.execute("SELECT * FROM destinos")

        return cursor.fetchall()

    finally:

        if cursor:
            cursor.close()

        if conexion:
            conexion.close()

def buscar_destino_por_id(id: int):

    conexion = None
    cursor = None

    try:

        conexion = obtener_conexion()
        cursor = conexion.cursor(dictionary=True)

        cursor.execute(
            "SELECT * FROM destinos WHERE id = %s",
            (id,)
        )

        return cursor.fetchone()

    finally:

        if cursor:
            cursor.close()

        if conexion:
            conexion.close()

def crear_destino(destino):

    conexion = None
    cursor = None

    try:

        conexion = obtener_conexion()
        cursor = conexion.cursor()

        sql = """
        INSERT INTO destinos
        (nombre, descripcion, ciudad, pais, precio, cupos_disponibles, imagen)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
        """

        valores = (
            destino.nombre,
            destino.descripcion,
            destino.ciudad,
            destino.pais,
            destino.precio,
            destino.cupos_disponibles,
            destino.imagen
        )

        cursor.execute(sql, valores)

        conexion.commit()

        return cursor.lastrowid

    finally:

        if cursor:
            cursor.close()

        if conexion:
            conexion.close()

def actualizar_destino(id: int, destino):

    conexion = None
    cursor = None

    try:

        conexion = obtener_conexion()
        cursor = conexion.cursor()

        sql = """
        UPDATE destinos
        SET nombre = %s,
            descripcion = %s,
            ciudad = %s,
            pais = %s,
            precio = %s,
            cupos_disponibles = %s,
            imagen = %s
        WHERE id = %s
        """

        valores = (
            destino.nombre,
            destino.descripcion,
            destino.ciudad,
            destino.pais,
            destino.precio,
            destino.cupos_disponibles,
            destino.imagen,
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