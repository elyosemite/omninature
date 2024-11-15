import requests
from config.settings import AUTH_TOKEN

def make_request(method, url, json=None):
    headers = {
        "Authorization": f"Bearer token_aqui",
        "Content-Type": "application/json",
        "Ocp-Apim-Subscription-Key": ""
    }
    response = requests.request(method, url, headers=headers, json=json)
    response.raise_for_status()
    return response
