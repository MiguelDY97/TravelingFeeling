const contenedor = document.getElementById("detalleDestino");

actualizarBarraSesion();

const parametros = new URLSearchParams(window.location.search);
const idDestino = parametros.get("id");

async function cargarDetalle() {

    if (!idDestino) {
        window.location.href = "destinos.html";
        return;
    }

    try {

        const destino = await obtenerDestinoPorId(idDestino);

        document.title = `${destino.nombre} - TravelingFeeling`;

        contenedor.innerHTML = `
            <div class="detalle-imagen imagen-con-badge">
                <img src="${rutaImagen(destino.imagen)}"
                     alt="${destino.nombre}"
                     onerror="this.onerror=null; this.src=generarImagenRespaldo('${destino.nombre.replace(/'/g, "")}');">
                <div class="badge-precio">$${Number(destino.precio).toLocaleString("es-CO")}</div>
            </div>
            <div class="detalle-info">
                <h1>${destino.nombre}</h1>
                <p class="detalle-ciudad"><i class="fa-solid fa-location-dot"></i> ${destino.ciudad}</p>
                <p class="detalle-descripcion">${destino.descripcion}</p>
                <div class="detalle-datos">
                    <div class="detalle-precio">$${Number(destino.precio).toLocaleString("es-CO")} <span>por persona</span></div>
                    <div class="detalle-cupos"><i class="fa-solid fa-ticket"></i> ${destino.cupos_disponibles} cupos disponibles</div>
                </div>
                <button class="boton-principal" onclick="irAReservar(${destino.id})">Reservar este destino</button>
            </div>
        `;

    } catch (error) {

        contenedor.innerHTML = `<p>Error al cargar el destino: ${error.message}</p>`;
    }
}

function irAReservar(idDestino) {

    if (!obtenerUsuarioActual()) {
        window.location.href = "login.html";
        return;
    }

    window.location.href = `reservar.html?id=${idDestino}`;
}

cargarDetalle();