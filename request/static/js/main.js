// Ожидаем, что у вас есть HTML элементы с id "add_application-tab" и "record-tab"
// для ваших вкладок "Оставить заявку" и "Мои заявки".
function openRecord() {
    const addApplicationTab = document.getElementById("add_application-tab");
    const recordTab = document.getElementById("record-tab");
    recordTab.classList.add("active");
    addApplicationTab.classList.remove("active");
    document.getElementById("record").classList.add("show");
    document.getElementById("add_application").classList.remove("show");
    document.getElementById("record").classList.add("active");
    document.getElementById("add_application").classList.remove("active");
}

function openAddApplication() {
    const addApplicationTab = document.getElementById("add_application-tab");
    const recordTab = document.getElementById("record-tab");
    addApplicationTab.classList.add("active");
    recordTab.classList.remove("active");
    document.getElementById("add_application").classList.add("show");
    document.getElementById("record").classList.remove("show");
    document.getElementById("add_application").classList.add("active");
    document.getElementById("record").classList.remove("active");
}

document.addEventListener("DOMContentLoaded", () => {
    const hash = window.location.hash;
    const addApplicationTab = document.getElementById("add_application-tab");
    const recordTab = document.getElementById("record-tab");

    if (addApplicationTab && recordTab) {
        addApplicationTab.addEventListener("click", () => openAddApplication());
        recordTab.addEventListener("click", () => openRecord());

        switch(hash) {
            case '#record':
                openRecord ()
                break;
            case '#add_application':
                openAddApplication ()
                break;
        }
    }
})


function editApplication(id) {
    console.log('Функция editApplication вызвана с id:', id);
    var editForms = document.querySelectorAll(".edit-form");
    editForms.forEach(function(form) {
        form.style.display = 'none';
    });

    var form = document.querySelector(".edit-form input[name=editId][value='" + id + "']").parentNode;
    form.style.display = 'block';
}
function cancelEdit(button) {
    var form = button.parentNode.parentNode;
    form.style.display = 'none';
}