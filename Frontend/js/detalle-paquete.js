const contenedor = document.getElementById("detallePaquete");

actualizarBarraSesion();

const parametros = new URLSearchParams(window.location.search);
const idPaquete = parametros.get("id");

async function cargarDetalle() {

    if (!idPaquete) {
        window.location.href = "paquetes.html";
        return;
    }

    try {

        const paquete = await obtenerPaquetePorId(idPaquete);

        document.title = `${paquete.nombre} - TravelingFeeling`;

        contenedor.innerHTML = `
            <div class="detalle-imagen imagen-con-badge">
                <img src="${rutaImagen(paquete.imagen)}"
                     alt="${paquete.nombre}"
                     onerror="this.onerror=null; this.src=generarImagenRespaldo('${paquete.nombre.replace(/'/g, "")}');">
                <div class="badge-precio">$${Number(paquete.precio).toLocaleString("es-CO")}</div>
            </div>
            <div class="detalle-info">
                <h1>${paquete.nombre}</h1>
                <p class="detalle-ciudad"><i class="fa-solid fa-calendar-days"></i> ${paquete.duracion_dias} días</p>
                <p class="detalle-descripcion">${paquete.descripcion}</p>
                <div class="detalle-datos">
                    <div class="detalle-precio">$${Number(paquete.precio).toLocaleString("es-CO")} <span>por persona</span></div>
                    <div class="detalle-cupos"><i class="fa-solid fa-ticket"></i> ${paquete.cupos_disponibles} cupos disponibles</div>
                </div>
                <button class="boton-principal" onclick="irAReservarPaquete(${paquete.id})">Reservar este paquete</button>
            </div>
        `;

    } catch (error) {

        contenedor.innerHTML = `<p>Error al cargar el paquete: ${error.message}</p>`;
    }
}

function irAReservarPaquete(idPaquete) {

    if (!obtenerUsuarioActual()) {
        window.location.href = "login.html";
        return;
    }

    window.location.href = `reservar.html?paquete=${idPaquete}`;
}

cargarDetalle();