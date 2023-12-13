let dataTable;
let dataTableInitialized = false;

const dataTableOptions = {
    pageLength: 4,
    destroy: true,
    language: {
        url: '//cdn.datatables.net/plug-ins/1.13.7/i18n/es-ES.json',
        lengthMenu: "Mostrar _MENU_ registros",
        info: "Mostrando de _START_ a _END_ de un total de _TOTAL_ registros",
    }
};

const initDataTable = async () => {
    if (dataTableInitialized) {
        dataTable.destroy();
    }

    dataTable = $(".table").DataTable(dataTableOptions);

    dataTableInitialized = true;
}

window.addEventListener("load", async () => {
    await initDataTable()
})

document.querySelector('.profile-container').addEventListener('click', function () {
    var profileOption = document.querySelector('.profile-option');
    if (profileOption.classList.contains('expand')) {
        profileOption.classList.remove('expand');
        profileOption.style.display = 'none';
    } else {
        profileOption.classList.add('expand');
        profileOption.style.display = 'flex';
    }
});

document.getElementById("txtTipoUsuario").onchange = function () {
    if (this.value === "Externo") {
        document.getElementById("interno").selected = true;
        document.getElementById("txtTipoPrestamo").disabled = true;
    }

    else {
        document.getElementById("interno").selected = false;
        document.getElementById("txtTipoPrestamo").disabled = false;
    }
};

const nombre = document.querySelector(".txtNombrePres");
const apellido = document.querySelector(".txtApellidoPres");
const semestre = document.querySelector(".txtSemestrePres");
const escuela = document.querySelector(".txtEscuelaPres");
const cedulaEstudiantes = document.querySelector(".cedulaEstudiantes");
const cedulaAcademicos = document.querySelector(".cedulaAcademicos");
const cedulaAdministrativos = document.querySelector(".cedulaAdministrativos");
const cedulaExternos = document.querySelector(".cedulaExternos");

cedulaEstudiantes.addEventListener("change", function () {
    let option = cedulaEstudiantes.options[cedulaEstudiantes.selectedIndex];
    nombre.value = option.getAttribute("data-nombre");
    apellido.value = option.getAttribute("data-apellido");
    semestre.value = option.getAttribute("data-semestre");
    escuela.value = option.getAttribute("data-escuela");
});

cedulaAcademicos.addEventListener("change", function () {
    let option = cedulaAcademicos.options[cedulaAcademicos.selectedIndex];
    nombre.value = option.getAttribute("data-nombre");
    apellido.value = option.getAttribute("data-apellido");
    escuela.value = option.getAttribute("data-escuela");
});

cedulaAdministrativos.addEventListener("change", function () {
    let option = cedulaAdministrativos.options[cedulaAdministrativos.selectedIndex];
    nombre.value = option.getAttribute("data-nombre");
    apellido.value = option.getAttribute("data-apellido");
});

document.getElementById("txtTipoUsuario").onchange = function () {
    // Selecciona el elemento anterior y quita la clase select-active si existe
    var previousElements = document.querySelectorAll(".select-active");
    previousElements.forEach(function (element) {
        element.classList.remove("select-active");
        element.setAttribute("name", " ")
    });

    if (this.value === "Estudiante") {
        cedulaEstudiantes.classList.add("select-active");
        cedulaEstudiantes.setAttribute("name", "txtCedula");
        semestre.classList.add("select-active");
        escuela.classList.add("select-active");
    } else if (this.value === "Académico") {
        cedulaAcademicos.classList.add("select-active");
        cedulaAcademicos.setAttribute("name", "txtCedula");
        escuela.classList.add("select-active");
    } else if (this.value === "Administrativo") {
        cedulaAdministrativos.classList.add("select-active");
        cedulaAdministrativos.setAttribute("name", "txtCedula");
    } else if (this.value === "Externo") {
        cedulaExternos.classList.add("select-active");
        cedulaExternos.setAttribute("name", "txtCedula");
    }

};

document.querySelector('.close').addEventListener('click', function () {
    this.parentNode.remove();
});

setTimeout(function () {
    document.querySelector('.error').classList.remove('error');
}, 5000);

