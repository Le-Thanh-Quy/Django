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

function calc(element, price, idCombobox, index, id_item, isCamera) {
    // let total_money = parseFloat(document.getElementById('payment_total').textContent)
    let value = parseFloat(document.getElementById(idCombobox).value);
    if (element.checked) {
        let price_now = total_money + parseFloat(price) * value
        var output_money = new Intl.NumberFormat('vi-VN', {style: 'currency', currency: 'VND'}).format(price_now);
        document.getElementById('payment_total').textContent = output_money + '';
        total_money = price_now
        sendData(index, true, id_item, isCamera);
    } else {
        let price_now = total_money - parseFloat(price) * value
        var output_money = new Intl.NumberFormat('vi-VN', {style: 'currency', currency: 'VND'}).format(price_now);
        document.getElementById('payment_total').textContent = output_money + '';
        total_money = price_now
        sendData(index, false, id_item , isCamera);
    }
}


function calCBB(element, price, idCheckbox, index, id_item, isCamera) {
    // var total_money = parseFloat(document.getElementById('payment_total').textContent)
    if (!document.getElementById(idCheckbox).checked) {
        price_now = total_money + parseFloat(price) * parseFloat(element.value)
        var output_money = new Intl.NumberFormat('vi-VN', {style: 'currency', currency: 'VND'}).format(price_now);
        document.getElementById('payment_total').textContent = output_money + '';
        total_money = price_now
        sendData(index, true, id_item, isCamera);
    } else {
        total_money = total_money - parseFloat(price) * parseFloat(element.oldvalue)
        price_now = total_money + parseFloat(price) * parseFloat(element.value)
        var output_money = new Intl.NumberFormat('vi-VN', {style: 'currency', currency: 'VND'}).format(price_now);
        document.getElementById('payment_total').textContent = output_money + '';
        total_money = price_now
        sendData(index, true, id_item, isCamera);
    }
    document.getElementById(idCheckbox).checked = true
}

function sendData(index, isChecked, id_item, isCamera) {
    var checkbox = document.getElementById('products' + index);
    var combobox = document.getElementById('combobox ' + index);
    var color = document.getElementById('input_19_custom_1001_1' + index);
    checkbox.value = id_item + " and " + combobox.value + " and " + color.value + " and " + isCamera
    if (isChecked) {
        checkbox.checked = true;
    } else {
        checkbox.checked = false;
    }
}

