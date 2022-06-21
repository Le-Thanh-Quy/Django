window.onscroll = function () {
    scrollFunction()
};

function scrollFunction() {
    if (document.body.scrollTop > 70 || document.documentElement.scrollTop > 70) {
        document.getElementById("myBtn").style.display = "block";
    } else {
        document.getElementById("myBtn").style.display = "none";
    }
}

// When the user clicks on the button, scroll to the top of the document
function topFunction() {
    window.scrollTo({top: 0, behavior: 'smooth'});
}


let isHide = true;

function onSearch() {
    if (isHide) {
        showInputSearch();
    } else {
        let searchContent = document.getElementById('input-search').value
        if (searchContent.toString() === "") {
            isHide = true;
            hideInputSearch();
        } else {
            window.location.href = '/' + searchContent + "/search";
        }

    }

}

function hideInputSearch() {
    document.getElementById('input-search').style.display = 'none'
}

function showInputSearch() {
    isHide = false;
    let inputSearch = document.getElementById('input-search');
    inputSearch.style.display = 'block'
    inputSearch.focus();
}
