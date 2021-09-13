async function getCoderData() {
    var response = await fetch("https://api.github.com/users/Carpe-liam");

    var data = await response.json();
    console.log(data);
    return data;
}

function get() {
    fetch("https://api.github.com/users/Carpe-liam")
        .then(response => response.json() )
        .then(coderData => console.log(coderData)   )
        .catch(err => console.log(err)  )
}