function showSlides(n) {
    let i;
    let slides = document.getElementsByClassName("mySlides");
    let dots = document.getElementsByClassName("dot-item");
    if (n > slides.length) {
        slideIndex = 1
    }
    if (n < 1) {
        slideIndex = slides.length
    }
    for (i = 0; i < slides.length; i++) {
        slides[i].style.display = "none";
    }
    for (i = 0; i < dots.length; i++) {
        dots[i].className = dots[i].className.replace(" active", "");
    }
    slides[slideIndex - 1].style.display = "block";
    dots[slideIndex - 1].className += " active";
}

function calc(element, price, idCombobox) {
    // let total_money = parseFloat(document.getElementById('payment_total').textContent)
    let value = parseFloat(document.getElementById(idCombobox).value);
    if (element.checked) {
        let price_now = total_money + parseFloat(price) * value
        document.getElementById('payment_total').textContent = price_now + '';
    total_money = price_now
    } else {
        let price_now = total_money - parseFloat(price) * value
        document.getElementById('payment_total').textContent = price_now + '';
    total_money = price_now
    }
}


function calCBB(element, price, idCheckbox) {
    // var total_money = parseFloat(document.getElementById('payment_total').textContent)
  if (!document.getElementById(idCheckbox).checked){
    price_now = total_money + parseFloat(price) * parseFloat(element.value)
    document.getElementById('payment_total').textContent = price_now + '';
    total_money = price_now
  } else {
    total_money = total_money - parseFloat(price) * parseFloat(element.oldvalue)
    price_now = total_money + parseFloat(price) * parseFloat(element.value)
    document.getElementById('payment_total').textContent = price_now + '';
    total_money = price_now
  }
    document.getElementById(idCheckbox).checked = true
}