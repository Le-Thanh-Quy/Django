var modal = document.getElementById("myModal");
var span = document.getElementsByClassName("close")[0];
span.onclick = function () {
    modal.style.display = "none";
}
window.onclick = function (event) {
    if (event.target == modal) {
        modal.style.display = "none";
    }
}

function openResetPassword() {
    var modal = document.getElementById("myModal");
    modal.style.display = "block"
    var password_input = document.getElementById("password");
    password_input.focus()
}
