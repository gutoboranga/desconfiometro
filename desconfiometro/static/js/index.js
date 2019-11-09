function getData(event) {
    let site = document.getElementById('search').value
    var url = new URL("http://localhost:5000/api"),
    
    params = {'url':site}
    
    Object.keys(params).forEach(key => url.searchParams.append(key, params[key]))
    
    fetch(url)
        .then((resp) => resp.text())
        .then(function(data) {
            document.getElementById('results_container').innerHTML = data
        })
}

