async function getCoderData() {
    var response = await fetch("https://api.github.com/users/Carpe-liam");

    var data = await response.json();
    console.log(data);
    getCoderData.addEventListener("load", loadData)
    return data;

}

function loadData() {
    document.getElementById('api').innerHTML = this.responseText
}


function loadAPI() {
    var xhttp = new XMLHttpRequest();
    xhttp.open("GET", "https://api.github.com/users/Carpe-liam", false);
    xhttp.addEventListener("load", loadData);
    xhttp.send();
}

  // Displaying the data
function loadData() {
    document.getElementById('api').innerText = this.responseText;
}


function get() {
    fetch("https://api.github.com/users/Carpe-liam")
        .then(response => response.json() )
        .then(coderData => console.log(coderData)   )
        .catch(err => console.log(err)  )
}
