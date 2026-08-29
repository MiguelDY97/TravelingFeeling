const usuarioActual = obtenerUsuarioActual();

if (!usuarioActual) {
    window.location.href = "login.html";
}

document.getElementById("botonSalir").addEventListener("click", cerrarSesion);

const listaReservas = document.getElementById("listaReservas");

async function cargarMisReservas() {

    try {

        const reservas = await obtenerReservasPorUsuario(usuarioActual.id);

        if (reservas.length === 0) {
            listaReservas.innerHTML = "<p>Todavía no tienes reservas.</p>";
            return;
        }

        const tarjetas = await Promise.all(
            reservas.map(async (reserva) => {

                let nombreDestino = `Destino #${reserva.id_destino}`;

                try {
                    const destino = await obtenerDestinoPorId(reserva.id_destino);
                    nombreDestino = destino.nombre;
                } catch (error) {
                    // Si el destino ya no existe, dejamos el texto de respaldo
                }

                return crearTarjetaReserva(reserva, nombreDestino);
            })
        );

        listaReservas.innerHTML = tarjetas.join("");

    } catch (error) {

        listaReservas.innerHTML = `<p>Error al cargar reservas: ${error.message}</p>`;
    }
}

function crearTarjetaReserva(reserva, nombreDestino) {

    const iconosEstado = {
        pendiente: "fa-clock",
        confirmada: "fa-circle-check",
        cancelada: "fa-circle-xmark"
    };

    return `
        <div class="tarjeta-destino">
            <div class="info">
                <h3>${nombreDestino}</h3>
                <p><i class="fa-solid fa-calendar-days"></i> ${reserva.fecha_reserva}</p>
                <p><i class="fa-solid fa-users"></i> ${reserva.cantidad_personas} personas</p>
                <div class="estado estado-${reserva.estado}">
                    <i class="fa-solid ${iconosEstado[reserva.estado] || 'fa-circle'}"></i>${reserva.estado}
                </div>
            </div>
        </div>
    `;
}

listaReservas.innerHTML = `<div class="cargando"><div class="spinner"></div><p>Cargando tus reservas...</p></div>`;
cargarMisReservas();