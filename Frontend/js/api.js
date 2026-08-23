const API_URL = "http://127.0.0.1:8000";

async function loginRequest(correo, contraseña) {

    const respuesta = await fetch(`${API_URL}/auth/login`, {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ correo, contraseña })
    });

    const datos = await respuesta.json();

    if (!respuesta.ok) {
        throw new Error(datos.detail || "Error al iniciar sesión");
    }

    return datos;
}

async function registrarUsuario(usuario) {

    const respuesta = await fetch(`${API_URL}/usuarios/`, {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(usuario)
    });

    const datos = await respuesta.json();

    if (!respuesta.ok) {
        throw new Error(datos.detail || "Error al registrar usuario");
    }

    return datos;
}

async function obtenerDestinos() {

    const respuesta = await fetch(`${API_URL}/destinos/`);

    const datos = await respuesta.json();

    if (!respuesta.ok) {
        throw new Error(datos.detail || "Error al obtener destinos");
    }

    return datos;
}

async function obtenerDestinoPorId(id) {

    const respuesta = await fetch(`${API_URL}/destinos/${id}`);

    const datos = await respuesta.json();

    if (!respuesta.ok) {
        throw new Error(datos.detail || "Error al obtener destino");
    }

    return datos;
}

async function crearReserva(reserva) {

    const respuesta = await fetch(`${API_URL}/reservas/`, {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
            "Authorization": `Bearer ${obtenerToken()}`
        },
        body: JSON.stringify(reserva)
    });

    const datos = await respuesta.json();

    if (!respuesta.ok) {
        throw new Error(datos.detail || "Error al crear reserva");
    }

    return datos;
}

async function obtenerReservasPorUsuario(idUsuario) {

    const respuesta = await fetch(`${API_URL}/reservas/usuario/${idUsuario}`, {
        headers: {
            "Authorization": `Bearer ${obtenerToken()}`
        }
    });

    const datos = await respuesta.json();

    if (!respuesta.ok) {
        throw new Error(datos.detail || "Error al obtener tus reservas");
    }

    return datos;
}

async function obtenerPaquetes() {

    const respuesta = await fetch(`${API_URL}/paquetes/`);

    const datos = await respuesta.json();

    if (!respuesta.ok) {
        throw new Error(datos.detail || "Error al obtener paquetes");
    }

    return datos;
}

function guardarSesion(token, usuario) {
    localStorage.setItem("token", token);
    localStorage.setItem("usuario", JSON.stringify(usuario));
}

function obtenerToken() {
    return localStorage.getItem("token");
}

function obtenerUsuarioActual() {
    const usuario = localStorage.getItem("usuario");
    return usuario ? JSON.parse(usuario) : null;
}

function cerrarSesion() {
    localStorage.removeItem("token");
    localStorage.removeItem("usuario");
    window.location.href = "login.html";
}

function actualizarBarraSesion() {

    const usuario = obtenerUsuarioActual();

    const saludo = document.getElementById("saludoUsuario");
    const botonSalir = document.getElementById("botonSalir");
    const enlaceLogin = document.getElementById("enlaceLogin");
    const enlaceMisReservas = document.getElementById("enlaceMisReservas");

    if (usuario) {

        if (saludo) saludo.textContent = `Hola, ${usuario.nombre}`;
        if (enlaceLogin) enlaceLogin.style.display = "none";
        if (enlaceMisReservas) enlaceMisReservas.style.display = "inline-block";

        if (botonSalir) {
            botonSalir.style.display = "inline-block";
            botonSalir.addEventListener("click", cerrarSesion);
        }

    } else {

        if (botonSalir) botonSalir.style.display = "none";
        if (enlaceMisReservas) enlaceMisReservas.style.display = "none";
    }
}