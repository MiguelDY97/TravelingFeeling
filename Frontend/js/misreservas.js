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

    return `
        <div class="tarjeta-destino">
            <div class="info">
                <h3>${nombreDestino}</h3>
                <p>Fecha: ${reserva.fecha_reserva}</p>
                <p>Personas: ${reserva.cantidad_personas}</p>
                <div class="precio">${reserva.estado}</div>
            </div>
        </div>
    `;
}

cargarMisReservas();