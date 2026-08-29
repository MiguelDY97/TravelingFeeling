const formLogin = document.getElementById("formLogin");
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

formLogin.addEventListener("submit", async (evento) => {

    evento.preventDefault(); 

    mensajeError.classList.remove("visible");

    const correo = document.getElementById("correo").value;
    const contraseña = inputContraseña.value;

    botonSubmit.disabled = true;
    botonSubmit.textContent = "Ingresando...";

    try {

        const respuesta = await loginRequest(correo, contraseña);

        guardarSesion(respuesta.token, respuesta.usuario);

        window.location.href = "destinos.html";

    } catch (error) {

        mensajeError.textContent = error.message;
        mensajeError.classList.add("visible");

        botonSubmit.disabled = false;
        botonSubmit.textContent = "Ingresar";
    }
});