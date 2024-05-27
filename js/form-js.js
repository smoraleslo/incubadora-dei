
function toggleEquipo(show) {
    document.getElementById('equipoFields').style.display = show ? 'block' : 'none';
}

function toggleProfesor(show) {
    document.getElementById('profesorFields').style.display = show ? 'block' : 'none';
}

function toggleExtracurricular(show) {
    document.getElementById('extracurricularFields').style.display = show ? 'block' : 'none';
}

function toggleProblema(show) {
    document.getElementById('problemaFields').style.display = show ? 'block' : 'none';
    document.getElementById('noProblemaFields').style.display = show ? 'none' : 'block';
}
