document.addEventListener("DOMContentLoaded", function () {
    inicializarBuscador();
    inicializarCheckboxes();
});

function inicializarBuscador() {
    var searchInput = document.getElementById("search-input");
    var materiasList = document.getElementById("materias-list");
    var materias = materiasList.getElementsByTagName("li");
    var noResultsMessage = document.getElementById("no-results-message");

    searchInput.addEventListener("keyup", function () {
        buscarMaterias(searchInput, materias, noResultsMessage);
    });
}

function buscarMaterias(searchInput, materias, noResultsMessage) {
    var searchTerm = searchInput.value.toLowerCase();
    var found = false;

    Array.prototype.forEach.call(materias, function (materia) {
        var materiaText = materia.textContent.toLowerCase();
        var isVisible = searchTerm === "" || materiaText.includes(searchTerm);
        materia.style.display = isVisible ? "" : "none";
        if (isVisible) found = true;
    });

    noResultsMessage.style.display = found ? "none" : "";
}

function inicializarCheckboxes() {
    var checkboxes = document.querySelectorAll(".checkbox-mat");

    function uncheckOthers(event) {
        for (var i = 0; i < checkboxes.length; i++) {
            if (checkboxes[i] !== event.target) {
                checkboxes[i].checked = false;
            }
        }
    }

    for (var i = 0; i < checkboxes.length; i++) {
        checkboxes[i].addEventListener("change", uncheckOthers);
    }
}