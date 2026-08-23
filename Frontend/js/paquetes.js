const grillaPaquetes = document.getElementById("grillaPaquetes");

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

    return `
        <div class="tarjeta-destino">
            <img src="${paquete.imagen || 'img/placeholder.jpg'}" alt="${paquete.nombre}">
            <div class="info">
                <h3>${paquete.nombre}</h3>
                <p>${paquete.duracion_dias} días</p>
                <p>${paquete.descripcion}</p>
                <div class="precio">$${Number(paquete.precio).toLocaleString("es-CO")}</div>
            </div>
        </div>
    `;
}

cargarPaquetes();