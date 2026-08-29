const grillaDestinos = document.getElementById("grillaDestinos");

actualizarBarraSesion();

async function cargarDestinos() {

    try {

        const destinos = await obtenerDestinos();

        if (destinos.length === 0) {
            grillaDestinos.innerHTML = "<p>No hay destinos disponibles.</p>";
            return;
        }

        grillaDestinos.innerHTML = destinos.map(crearTarjetaDestino).join("");

    } catch (error) {

        grillaDestinos.innerHTML = `<p>Error al cargar destinos: ${error.message}</p>`;
    }
}

function crearTarjetaDestino(destino) {

    const nombreSeguro = destino.nombre.replace(/'/g, "");

    return `
        <div class="tarjeta-destino">
            <a href="detalle.html?id=${destino.id}" class="imagen-con-badge">
                <img src="${rutaImagen(destino.imagen)}" alt="${destino.nombre}"
                     onerror="this.onerror=null; this.src=generarImagenRespaldo('${nombreSeguro}');">
                <div class="badge-precio">$${Number(destino.precio).toLocaleString("es-CO")}</div>
            </a>
            <div class="info">
                <h3><a href="detalle.html?id=${destino.id}">${destino.nombre}</a></h3>
                <p><i class="fa-solid fa-location-dot"></i> ${destino.ciudad}</p>
                <p>${destino.descripcion}</p>
                <button class="boton-principal" onclick="irAReservar(${destino.id})">Reservar</button>
            </div>
        </div>
    `;
}

function irAReservar(idDestino) {

    if (!obtenerUsuarioActual()) {
        window.location.href = "login.html";
        return;
    }

    window.location.href = `reservar.html?id=${idDestino}`;
}

grillaDestinos.innerHTML = `<div class="cargando"><div class="spinner"></div><p>Cargando destinos...</p></div>`;
cargarDestinos();