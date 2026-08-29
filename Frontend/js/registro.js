const formRegistro = document.getElementById("formRegistro");
const mensajeError = document.getElementById("mensajeError");
const botonSubmit = document.getElementById("botonSubmit");
const botonOjo = document.getElementById("botonOjo");
const inputContraseña = document.getElementById("contraseña");

botonOjo.addEventListener("click", () => {

    const mostrando = inputContraseña.type === "text";

    inputContraseña.type = mostrando ? "password" : "text";
    botonOjo.innerHTML = mostrando
        ? '<i class="fa-solid fa-eye"></i>'
        : '<i class="fa-solid fa-eye-slash"></i>';
});

formRegistro.addEventListener("submit", async (evento) => {

    evento.preventDefault();

    mensajeError.classList.remove("visible");

    const nuevoUsuario = {
        nombre: document.getElementById("nombre").value,
        apellido: document.getElementById("apellido").value,
        correo: document.getElementById("correo").value,
        telefono: document.getElementById("telefono").value,
        contraseña: inputContraseña.value
    };

    botonSubmit.disabled = true;
    botonSubmit.textContent = "Creando cuenta...";

    try {

        await registrarUsuario(nuevoUsuario);

        window.location.href = "login.html";

    } catch (error) {

        mensajeError.textContent = error.message;
        mensajeError.classList.add("visible");

        botonSubmit.disabled = false;
        botonSubmit.textContent = "Registrarme";
    }
});