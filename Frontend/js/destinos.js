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

    return `
        <div class="tarjeta-destino">
            <img src="${destino.imagen || 'img/placeholder.jpg'}" alt="${destino.nombre}">
            <div class="info">
                <h3>${destino.nombre}</h3>
                <p>${destino.ciudad}</p>
                <p>${destino.descripcion}</p>
                <div class="precio">$${Number(destino.precio).toLocaleString("es-CO")}</div>
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

cargarDestinos();