function getData(event) {
    let url = "http://localhost:5000/api";
    
    fetch(url)
    .then((resp) => resp.text())
    .then(function(data) {
        document.getElementById('results_container').innerHTML = data
    })
}

