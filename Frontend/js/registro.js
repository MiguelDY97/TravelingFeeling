const formRegistro = document.getElementById("formRegistro");
const mensajeError = document.getElementById("mensajeError");

formRegistro.addEventListener("submit", async (evento) => {

    evento.preventDefault();

    mensajeError.classList.remove("visible");

    const nuevoUsuario = {
        nombre: document.getElementById("nombre").value,
        apellido: document.getElementById("apellido").value,
        correo: document.getElementById("correo").value,
        telefono: document.getElementById("telefono").value,
        contraseña: document.getElementById("contraseña").value
    };

    try {

        await registrarUsuario(nuevoUsuario);

        window.location.href = "login.html";

    } catch (error) {

        mensajeError.textContent = error.message;
        mensajeError.classList.add("visible");
    }
});