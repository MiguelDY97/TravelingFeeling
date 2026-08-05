from database.conexion import obtener_conexion

def obtener_reservas():
    conexion = obtener_conexion()
    cursor = conexion.cursor(dictionary=True)

    cursor.execute("SELECT * FROM reservas")
    reservas = cursor.fetchall()

    cursor.close()
    conexion.close()

    return reservas


def obtener_reserva_por_id(id):
    conexion = obtener_conexion()
    cursor = conexion.cursor(dictionary=True)

    cursor.execute("SELECT * FROM reservas WHERE id = %s", (id,))
    reserva = cursor.fetchone()

    cursor.close()
    conexion.close()

    return reserva


def crear_reserva(reserva):
    conexion = obtener_conexion()
    cursor = conexion.cursor()

    sql = """
    INSERT INTO reservas
    (id_usuario, id_destino, fecha_reserva, cantidad_personas, estado)
    VALUES (%s, %s, %s, %s, %s)
    """

    valores = (
        reserva.id_usuario,
        reserva.id_destino,
        reserva.fecha_reserva,
        reserva.cantidad_personas,
        reserva.estado
    )

    cursor.execute(sql, valores)
    conexion.commit()

    cursor.close()
    conexion.close()


def actualizar_reserva(id, reserva):
    conexion = obtener_conexion()
    cursor = conexion.cursor()

    sql = """
    UPDATE reservas
    SET id_usuario=%s,
        id_destino=%s,
        fecha_reserva=%s,
        cantidad_personas=%s,
        estado=%s
    WHERE id=%s
    """

    valores = (
        reserva.id_usuario,
        reserva.id_destino,
        reserva.fecha_reserva,
        reserva.cantidad_personas,
        reserva.estado,
        id
    )

    cursor.execute(sql, valores)
    conexion.commit()

    filas = cursor.rowcount

    cursor.close()
    conexion.close()

    return filas


def eliminar_reserva(id):
    conexion = obtener_conexion()
    cursor = conexion.cursor()

    cursor.execute("DELETE FROM reservas WHERE id=%s", (id,))
    conexion.commit()

    filas = cursor.rowcount

    cursor.close()
    conexion.close()

    return filas