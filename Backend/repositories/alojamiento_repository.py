from database.conexion import obtener_conexion

def obtener_alojamientos():

    conexion = None
    cursor = None

    try:

        conexion = obtener_conexion()
        cursor = conexion.cursor(dictionary=True)

        cursor.execute("SELECT * FROM alojamientos")

        return cursor.fetchall()

    finally:

        if cursor:
            cursor.close()

        if conexion:
            conexion.close()

def obtener_alojamiento_por_id(id: int):

    conexion = None
    cursor = None

    try:

        conexion = obtener_conexion()
        cursor = conexion.cursor(dictionary=True)

        cursor.execute(
            "SELECT * FROM alojamientos WHERE id = %s",
            (id,)
        )

        return cursor.fetchone()

    finally:

        if cursor:
            cursor.close()

        if conexion:
            conexion.close()

def crear_alojamiento(alojamiento):

    conexion = None
    cursor = None

    try:

        conexion = obtener_conexion()
        cursor = conexion.cursor()

        sql = """
        INSERT INTO alojamientos
        (nombre, descripcion, ciudad, precio, capacidad_personas, cupos_disponibles, imagen)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
        """

        valores = (
            alojamiento.nombre,
            alojamiento.descripcion,
            alojamiento.ciudad,
            alojamiento.precio,
            alojamiento.capacidad_personas,
            alojamiento.cupos_disponibles,
            alojamiento.imagen
        )

        cursor.execute(sql, valores)

        conexion.commit()

        return cursor.lastrowid

    finally:

        if cursor:
            cursor.close()

        if conexion:
            conexion.close()

def actualizar_alojamiento(id: int, alojamiento):

    conexion = None
    cursor = None

    try:

        conexion = obtener_conexion()
        cursor = conexion.cursor()

        sql = """
        UPDATE alojamientos
        SET nombre = %s,
            descripcion = %s,
            ciudad = %s,
            precio = %s,
            capacidad_personas = %s,
            cupos_disponibles = %s,
            imagen = %s
        WHERE id = %s
        """

        valores = (
            alojamiento.nombre,
            alojamiento.descripcion,
            alojamiento.ciudad,
            alojamiento.precio,
            alojamiento.capacidad_personas,
            alojamiento.cupos_disponibles,
            alojamiento.imagen,
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

def eliminar_alojamiento(id: int):

    conexion = None
    cursor = None

    try:

        conexion = obtener_conexion()
        cursor = conexion.cursor()

        cursor.execute(
            "DELETE FROM alojamientos WHERE id = %s",
            (id,)
        )

        conexion.commit()

        return cursor.rowcount

    finally:

        if cursor:
            cursor.close()

        if conexion:
            conexion.close()