function toggleEquipo(show) {
    document.getElementById('equipoFields').style.display = show ? 'block' : 'none';
}

function toggleProfesor(show) {
    document.getElementById('profesorFields').style.display = show ? 'block' : 'none';
}


function toggleExtracurricular(show) {
    document.getElementById('extracurricularFields').style.display = show ? 'block' : 'none';
}

function updateSelectedTalleres() {
    const checkboxes = document.querySelectorAll('input[name="talleres"]:checked');
    const selectedList = document.getElementById('selectedTalleres');
    selectedList.innerHTML = ''; // Clear the list

    checkboxes.forEach((checkbox) => {
        const listItem = document.createElement('li');
        listItem.className = 'list-group-item';
        listItem.textContent = checkbox.nextElementSibling.textContent;
        selectedList.appendChild(listItem);
    });
}


function toggleProblema(show) {
    document.getElementById('problemaFields').style.display = show ? 'block' : 'none';
    document.getElementById('noProblemaFields').style.display = show ? 'none' : 'block';
}
