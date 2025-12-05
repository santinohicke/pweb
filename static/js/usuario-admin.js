document.addEventListener("DOMContentLoaded", function () {
    var formulario = document.getElementById("login-adm");

    formulario.addEventListener("submit", function (event) {
        var tipoUsuario = document.getElementsByName("tipo_usuario")[0].value;
        var email = document.getElementsByName("email")[0].value;
        var nombre = document.getElementsByName("nombre_completo")[0].value;
        var contraseña = document.getElementsByName("contraseña")[0].value;
        var legajo = document.getElementsByName("legajo")[0].value;

        if (tipoUsuario === "" || email === "" || nombre === "" || contraseña === "" || legajo === "") {
            alert("Todos los campos son obligatorios.");
            event.preventDefault(); // Evita que el formulario se envíe
        }
    });
});
