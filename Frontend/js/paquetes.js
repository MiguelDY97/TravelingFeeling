const grillaPaquetes = document.getElementById("grillaPaquetes");

actualizarBarraSesion();

async function cargarPaquetes() {

    try {

        const paquetes = await obtenerPaquetes();

        if (paquetes.length === 0) {
            grillaPaquetes.innerHTML = "<p>No hay paquetes disponibles.</p>";
            return;
        }

        grillaPaquetes.innerHTML = paquetes.map(crearTarjetaPaquete).join("");

    } catch (error) {

        grillaPaquetes.innerHTML = `<p>Error al cargar paquetes: ${error.message}</p>`;
    }
}

function crearTarjetaPaquete(paquete) {

    const nombreSeguro = paquete.nombre.replace(/'/g, "");

    return `
        <div class="tarjeta-destino">
            <a href="detalle-paquete.html?id=${paquete.id}" class="imagen-con-badge">
                <img src="${rutaImagen(paquete.imagen)}" alt="${paquete.nombre}"
                     onerror="this.onerror=null; this.src=generarImagenRespaldo('${nombreSeguro}');">
                <div class="badge-precio">$${Number(paquete.precio).toLocaleString("es-CO")}</div>
            </a>
            <div class="info">
                <h3><a href="detalle-paquete.html?id=${paquete.id}">${paquete.nombre}</a></h3>
                <p><i class="fa-solid fa-calendar-days"></i> ${paquete.duracion_dias} días</p>
                <p>${paquete.descripcion}</p>
                <button class="boton-principal" onclick="irAReservarPaquete(${paquete.id})">Reservar</button>
            </div>
        </div>
    `;
}

function irAReservarPaquete(idPaquete) {

    if (!obtenerUsuarioActual()) {
        window.location.href = "login.html";
        return;
    }

    window.location.href = `reservar.html?paquete=${idPaquete}`;
}

grillaPaquetes.innerHTML = `<div class="cargando"><div class="spinner"></div><p>Cargando paquetes...</p></div>`;
cargarPaquetes();