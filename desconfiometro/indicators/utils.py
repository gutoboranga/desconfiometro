import requests


def get_registro_br(domain):
    url_request = "https://rdap.registro.br/domain/" + domain
    try:
        req = requests.get(url=url_request, timeout=2)
        if req.status_code != 404:
            return req.json()
        else:
            return ""
    except:
        return None
