import requests


def get_registro_br(domain):
    url_request = "https://rdap.registro.br/domain/" + domain
    print("VOU TENTAR PEGAR O registro_br")
    try:
        req = requests.get(url=url_request, timeout=2)
        print("OK")
        if req.status_code != 404:
            print("NOT 404")
            return req.json()
        else:
            print("ELSE")
            return ""
    except:
        print("EXCEPT")
        return None
