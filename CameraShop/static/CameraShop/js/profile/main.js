var modal = document.getElementById("myModal");
var modal1 = document.getElementById("myModalHistory");
var span = document.getElementsByClassName("close")[0];
span.onclick = function () {
    modal.style.display = "none";
}

var span1 = document.getElementsByClassName("close")[1];
span1.onclick = function () {
    modal1.style.display = "none";
}


window.onclick = function (event) {
    if (event.target == modal) {
        modal.style.display = "none";
    } else if (event.target == modal1) {
        modal1.style.display = "none";
    }
}

function openResetPassword() {
    var modal = document.getElementById("myModal");
    modal.style.display = "block"
    var password_input = document.getElementById("password");
    password_input.focus()
}


function openHistory() {
    var modal = document.getElementById("myModalHistory");
    modal.style.display = "block"
}