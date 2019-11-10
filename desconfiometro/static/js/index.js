var hasLiked = false
var likeValue = false

function getData(event) {
    let site = document.getElementById('search').value
    
    if (site == "" || site == undefined) { return }
    
    var url = new URL("http://localhost:5000/api"),
    
    params = {'url':site}
    
    Object.keys(params).forEach(key => url.searchParams.append(key, params[key]))
    
    startLoading()
    fetch(url)
        .then((resp) => resp.text())
        .then(function(data) {
            document.getElementById('results_container').innerHTML = data
            
            let element = document.getElementById("results_container")
            element.scrollIntoView(true)
        })
        .then(function(r) {
            stopLoading()
        });
}

function startLoading() {
    let body = document.getElementsByTagName('body')[0];
    let spinner = document.createElement("div");
    let alpha = document.createElement("div");

    alpha.id = 'alpha'
    spinner.id = 'spinner'
    
    alpha.appendChild(spinner)
    body.appendChild(alpha)
}

function stopLoading() {
    let alpha = document.getElementById('alpha');
    alpha.parentNode.removeChild(alpha)
}

function like() {
    setLike(true)
}

function dislike() {
    setLike(false)
}

function setLike(b) {
    hasLiked = true
    likeValue = b
    
    let likeName = b ? "like-selected" : "like"
    let dislikeName = b ? "dislike" : "dislike-selected"
    
    document.getElementById('like-img').src = "https://raw.githubusercontent.com/gutoboranga/public/master/" + likeName + ".png"
    document.getElementById('dislike-img').src = "https://raw.githubusercontent.com/gutoboranga/public/master/" + dislikeName + ".png"
}
