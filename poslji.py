import requests
def posljiUZ(razd, url, endpoint, apikey):
    headers = {
        "Authorization" : "Bearer " + apikey
    }
    data = {
        "distance": razd
    }
    response = requests.post(url+endpoint, json=data, headers=headers)
    print(response.status_code)#ce je 200 je ok, ce pa kar kol druzga pa ne ok

def posljiDHT(dhtData, url, endpoint, apikey):
    headers = {
        "Authorization" : "Bearer " + apikey
    }
    data = {
        "temp": dhtData[1]
        "hum": dhtData[0]
    }
    response = requests.post(url+endpoint, json=data, headers=headers)
    print(response.status_code)#ce je 200 je ok, ce pa kar kol druzga pa ne ok

def posljiPIR():
    headers = {
        "Authorization" : "Bearer " + apikey
    }
    data = {
        "temp": dhtData[1]
        "hum": dhtData[0]
    }