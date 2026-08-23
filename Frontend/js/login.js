const formLogin = document.getElementById("formLogin");
const mensajeError = document.getElementById("mensajeError");

formLogin.addEventListener("submit", async (evento) => {

    evento.preventDefault(); // evita que el formulario recargue la pagina

    mensajeError.classList.remove("visible");

    const correo = document.getElementById("correo").value;
    const contraseña = document.getElementById("contraseña").value;

    try {

        const respuesta = await loginRequest(correo, contraseña);

        guardarSesion(respuesta.token, respuesta.usuario);

        window.location.href = "destinos.html";

    } catch (error) {

        mensajeError.textContent = error.message;
        mensajeError.classList.add("visible");
    }
});