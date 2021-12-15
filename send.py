# to NI v while zanki
import requests
import Adafruit_DHT

DHT_SENSOR = Adafruit_DHT.DHT11
DHT_PIN = 4
url = "https://GraceWebApp-SebastjanTekavc.online404.repl.co"
apikey = "sebastjan"

headers = {
        "Authorization" : "Bearer " + apikey
}

while True:
    humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)

    if humidity is not None and temperature is not None:
        print("Temperatura je", temperature, "vlaga pa znaša", humidity)
        # to JE v while zanki
        data = {
                "temp": temperature,
                "hum": humidity
        }

        response = requests.post(url, json=data, headers=headers)
        print(response.status_code) # če bo napaka: 500, če bo v redu: 200
    else:
        print("Ni bilo mogoče uspostaviti komuinikacije s senzorjem, preverite povezavo.")
        print("Najverjetneje so žice narobe povezane")
