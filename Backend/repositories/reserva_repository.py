from database.conexion import obtener_conexion

def obtener_reservas():

    conexion = None
    cursor = None

    try:

        conexion = obtener_conexion()
        cursor = conexion.cursor(dictionary=True)

        cursor.execute("SELECT * FROM reservas")

        return cursor.fetchall()

    finally:

        if cursor:
            cursor.close()

        if conexion:
            conexion.close()

def obtener_reservas_por_usuario(id_usuario: int):

    conexion = None
    cursor = None

    try:

        conexion = obtener_conexion()
        cursor = conexion.cursor(dictionary=True)

        cursor.execute(
            "SELECT * FROM reservas WHERE id_usuario = %s",
            (id_usuario,)
        )

        return cursor.fetchall()

    finally:

        if cursor:
            cursor.close()

        if conexion:
            conexion.close()

def obtener_reserva_por_id(id: int):

    conexion = None
    cursor = None

    try:

        conexion = obtener_conexion()
        cursor = conexion.cursor(dictionary=True)

        cursor.execute(
            "SELECT * FROM reservas WHERE id = %s",
            (id,)
        )

        return cursor.fetchone()

    finally:

        if cursor:
            cursor.close()

        if conexion:
            conexion.close()

def crear_reserva(reserva):

    conexion = None
    cursor = None

    try:

        conexion = obtener_conexion()
        cursor = conexion.cursor()

        sql = """
        INSERT INTO reservas
        (id_usuario, id_destino, id_paquete, fecha_reserva, cantidad_personas, estado)
        VALUES (%s, %s, %s, %s, %s, %s)
        """

        valores = (
            reserva.id_usuario,
            reserva.id_destino,
            reserva.id_paquete,
            reserva.fecha_reserva,
            reserva.cantidad_personas,
            reserva.estado
        )

        cursor.execute(sql, valores)

        conexion.commit()

        return cursor.lastrowid

    finally:

        if cursor:
            cursor.close()

        if conexion:
            conexion.close()

def actualizar_reserva(id: int, reserva):

    conexion = None
    cursor = None

    try:

        conexion = obtener_conexion()
        cursor = conexion.cursor()

        sql = """
        UPDATE reservas
        SET id_usuario = %s,
            id_destino = %s,
            id_paquete = %s,
            fecha_reserva = %s,
            cantidad_personas = %s,
            estado = %s
        WHERE id = %s
        """

        valores = (
            reserva.id_usuario,
            reserva.id_destino,
            reserva.id_paquete,
            reserva.fecha_reserva,
            reserva.cantidad_personas,
            reserva.estado,
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

def eliminar_reserva(id: int):

    conexion = None
    cursor = None

    try:

        conexion = obtener_conexion()
        cursor = conexion.cursor()

        cursor.execute(
            "DELETE FROM reservas WHERE id = %s",
            (id,)
        )

        conexion.commit()

        return cursor.rowcount

    finally:

        if cursor:
            cursor.close()

        if conexion:
            conexion.close()