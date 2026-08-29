const usuarioActual = obtenerUsuarioActual();

if (!usuarioActual) {
    window.location.href = "login.html";
}

const parametros = new URLSearchParams(window.location.search);
const idDestinoParam = parametros.get("id");
const idPaqueteParam = parametros.get("paquete");

if (!idDestinoParam && !idPaqueteParam) {
    window.location.href = "destinos.html";
}

const tituloDestino = document.getElementById("tituloDestino");
const formReservar = document.getElementById("formReservar");
const mensajeError = document.getElementById("mensajeError");

document.getElementById("fecha_reserva").min = new Date().toISOString().split("T")[0];

let idDestinoResuelto = idDestinoParam ? Number(idDestinoParam) : null;
let idPaqueteResuelto = idPaqueteParam ? Number(idPaqueteParam) : null;

async function cargarInformacion() {

    try {

        if (idPaqueteParam) {

            const paquete = await obtenerPaquetePorId(idPaqueteParam);
            idDestinoResuelto = paquete.id_destino;
            tituloDestino.textContent = `Reservar paquete: ${paquete.nombre}`;

        } else {

            const destino = await obtenerDestinoPorId(idDestinoParam);
            tituloDestino.textContent = `Reservar: ${destino.nombre}`;
        }

    } catch (error) {

        tituloDestino.textContent = "Reservar";
    }
}

formReservar.addEventListener("submit", async (evento) => {

    evento.preventDefault();

    mensajeError.classList.remove("visible");

    const nuevaReserva = {
        id_usuario: usuarioActual.id,
        id_destino: idDestinoResuelto,
        id_paquete: idPaqueteResuelto,
        fecha_reserva: document.getElementById("fecha_reserva").value,
        cantidad_personas: Number(document.getElementById("cantidad_personas").value),
        estado: "pendiente"
    };

    try {

        await crearReserva(nuevaReserva);

        alert("Reserva creada correctamente");
        window.location.href = "misreservas.html";

    } catch (error) {

        mensajeError.textContent = error.message;
        mensajeError.classList.add("visible");
    }
});

cargarInformacion();