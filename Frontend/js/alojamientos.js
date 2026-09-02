const grillaAlojamientos = document.getElementById("grillaAlojamientos");

actualizarBarraSesion();

async function cargarAlojamientos() {

    try {

        const alojamientos = await obtenerAlojamientos();

        if (alojamientos.length === 0) {
            grillaAlojamientos.innerHTML = "<p>No hay alojamientos disponibles.</p>";
            return;
        }

        grillaAlojamientos.innerHTML = alojamientos.map(crearTarjetaAlojamiento).join("");

    } catch (error) {

        grillaAlojamientos.innerHTML = `<p>Error al cargar alojamientos: ${error.message}</p>`;
    }
}

function crearTarjetaAlojamiento(alojamiento) {

    const nombreSeguro = alojamiento.nombre.replace(/'/g, "");

    return `
        <div class="tarjeta-destino">
            <a href="detalle-alojamiento.html?id=${alojamiento.id}" class="imagen-con-badge">
                <img src="${rutaImagen(alojamiento.imagen)}" alt="${alojamiento.nombre}"
                     onerror="this.onerror=null; this.src=generarImagenRespaldo('${nombreSeguro}');">
                <div class="badge-precio">$${Number(alojamiento.precio).toLocaleString("es-CO")}</div>
            </a>
            <div class="info">
                <h3><a href="detalle-alojamiento.html?id=${alojamiento.id}">${alojamiento.nombre}</a></h3>
                <p><i class="fa-solid fa-location-dot"></i> ${alojamiento.ciudad}</p>
                <p><i class="fa-solid fa-users"></i> Hasta ${alojamiento.capacidad_personas} personas</p>
                <a href="detalle-alojamiento.html?id=${alojamiento.id}" class="boton-principal" style="display:block; text-align:center; text-decoration:none;">Ver más</a>
            </div>
        </div>
    `;
}

cargarAlojamientos();