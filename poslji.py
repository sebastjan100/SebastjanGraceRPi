import requests
def posljiUZ(razd, url, endpoint, apikey):
    headers = {
        "Authorization" : "Bearer " + apikey
    }
    data = {
        "distance" : razd
    }
    print(url+endpoint)
    print(headers)
    print(apikey)
    response = requests.post(url+endpoint, json=data, headers=headers)
    print(response.status_code)

def posljiDHT(dhtData, url, endpoint, apikey):
    print("test")