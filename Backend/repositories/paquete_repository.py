from database.conexion import obtener_conexion

def obtener_paquetes():

    conexion = None
    cursor = None

    try:

        conexion = obtener_conexion()
        cursor = conexion.cursor(dictionary=True)

        cursor.execute("SELECT * FROM paquetes")

        return cursor.fetchall()

    finally:

        if cursor:
            cursor.close()

        if conexion:
            conexion.close()

def obtener_paquete_por_id(id: int):

    conexion = None
    cursor = None

    try:

        conexion = obtener_conexion()
        cursor = conexion.cursor(dictionary=True)

        cursor.execute(
            "SELECT * FROM paquetes WHERE id = %s",
            (id,)
        )

        return cursor.fetchone()

    finally:

        if cursor:
            cursor.close()

        if conexion:
            conexion.close()

def crear_paquete(paquete):

    conexion = None
    cursor = None

    try:

        conexion = obtener_conexion()
        cursor = conexion.cursor()

        sql = """
        INSERT INTO paquetes
        (id_destino, nombre, descripcion, duracion_dias, precio, cupos_disponibles, imagen)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
        """

        valores = (
            paquete.id_destino,
            paquete.nombre,
            paquete.descripcion,
            paquete.duracion_dias,
            paquete.precio,
            paquete.cupos_disponibles,
            paquete.imagen
        )

        cursor.execute(sql, valores)

        conexion.commit()

        return cursor.lastrowid

    finally:

        if cursor:
            cursor.close()

        if conexion:
            conexion.close()

def actualizar_paquete(id: int, paquete):

    conexion = None
    cursor = None

    try:

        conexion = obtener_conexion()
        cursor = conexion.cursor()

        sql = """
        UPDATE paquetes
        SET id_destino = %s,
            nombre = %s,
            descripcion = %s,
            duracion_dias = %s,
            precio = %s,
            cupos_disponibles = %s,
            imagen = %s
        WHERE id = %s
        """

        valores = (
            paquete.id_destino,
            paquete.nombre,
            paquete.descripcion,
            paquete.duracion_dias,
            paquete.precio,
            paquete.cupos_disponibles,
            paquete.imagen,
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

def eliminar_paquete(id: int):

    conexion = None
    cursor = None

    try:

        conexion = obtener_conexion()
        cursor = conexion.cursor()

        cursor.execute(
            "DELETE FROM paquetes WHERE id = %s",
            (id,)
        )

        conexion.commit()

        return cursor.rowcount

    finally:

        if cursor:
            cursor.close()

        if conexion:
            conexion.close()