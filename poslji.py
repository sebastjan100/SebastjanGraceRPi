import requests
def posljiUZ(razd, url, endpoint, apikey):
    headers = {
        "Authorization" : "Bearer " + apikey
    }
    dat = {
        "distance": razd
    }
    response = requests.post(url+endpoint, json=dat, headers=headers)
    print(response.status_code)#ce je 200 je ok, ce pa kar kol druzga pa ne ok

def posljiDHT():
    print("poslano DHT")