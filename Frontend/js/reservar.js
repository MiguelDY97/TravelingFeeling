const usuarioActual = obtenerUsuarioActual();

if (!usuarioActual) {
    window.location.href = "login.html";
}

const parametros = new URLSearchParams(window.location.search);
const idDestino = parametros.get("id");

if (!idDestino) {
    window.location.href = "index.html";
}

const tituloDestino = document.getElementById("tituloDestino");
const formReservar = document.getElementById("formReservar");
const mensajeError = document.getElementById("mensajeError");

async function cargarNombreDestino() {

    try {

        const destino = await obtenerDestinoPorId(idDestino);
        tituloDestino.textContent = `Reservar: ${destino.nombre}`;

    } catch (error) {

        tituloDestino.textContent = "Reservar";
    }
}

formReservar.addEventListener("submit", async (evento) => {

    evento.preventDefault();

    mensajeError.classList.remove("visible");

    const nuevaReserva = {
        id_usuario: usuarioActual.id,
        id_destino: Number(idDestino),
        fecha_reserva: document.getElementById("fecha_reserva").value,
        cantidad_personas: Number(document.getElementById("cantidad_personas").value),
        estado: "pendiente"
    };

    try {

        await crearReserva(nuevaReserva);

        alert("Reserva creada correctamente");
        window.location.href = "index.html";

    } catch (error) {

        mensajeError.textContent = error.message;
        mensajeError.classList.add("visible");
    }
});

cargarNombreDestino();