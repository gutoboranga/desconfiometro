import requests


def get_registro_br(parsed_url):
    url_request = "https://rdap.registro.br/domain/" + parsed_url.netloc
    print("request")
    try:
        req = requests.get(url=url_request, timeout=2)
        if(req.status_code != 404):
            return print(req.json())
        else:
            return ""
    except:
        return None
