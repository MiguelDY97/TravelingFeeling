const contenedor = document.getElementById("detalleAlojamiento");

actualizarBarraSesion();

const parametros = new URLSearchParams(window.location.search);
const idAlojamiento = parametros.get("id");

async function cargarDetalle() {

    if (!idAlojamiento) {
        window.location.href = "alojamientos.html";
        return;
    }

    try {

        const alojamiento = await obtenerAlojamientoPorId(idAlojamiento);

        document.title = `${alojamiento.nombre} - TravelingFeeling`;

        const mensajeWhatsapp = encodeURIComponent(
            `Hola, quiero mas información sobre ${alojamiento.nombre}`
        );

        contenedor.innerHTML = `
            <div class="detalle-imagen imagen-con-badge">
                <img src="${rutaImagen(alojamiento.imagen)}"
                     alt="${alojamiento.nombre}"
                     onerror="this.onerror=null; this.src=generarImagenRespaldo('${alojamiento.nombre.replace(/'/g, "")}');">
                <div class="badge-precio">$${Number(alojamiento.precio).toLocaleString("es-CO")}</div>
            </div>
            <div class="detalle-info">
                <h1>${alojamiento.nombre}</h1>
                <p class="detalle-ciudad"><i class="fa-solid fa-location-dot"></i> ${alojamiento.ciudad}</p>
                <p class="detalle-descripcion">${alojamiento.descripcion}</p>
                <div class="detalle-datos">
                    <div class="detalle-precio">$${Number(alojamiento.precio).toLocaleString("es-CO")}</div>
                    <div class="detalle-cupos"><i class="fa-solid fa-users"></i> Hasta ${alojamiento.capacidad_personas} personas</div>
                </div>
                <a href="https://wa.me/573148072654?text=${mensajeWhatsapp}" target="_blank" class="boton-principal" style="display:block; text-align:center; text-decoration:none; background-color:#25D366;">
                    <i class="fa-brands fa-whatsapp"></i> Consultar disponibilidad
                </a>
            </div>
        `;

    } catch (error) {

        contenedor.innerHTML = `<p>Error al cargar el alojamiento: ${error.message}</p>`;
    }
}

cargarDetalle();