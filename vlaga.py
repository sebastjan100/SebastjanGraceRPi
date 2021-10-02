import Adafruit_DHT

DHT_SENSOR = Adafruit_DHT.DHT11
DHT_PIN = 4

while True:
    humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)

    if humidity is not None and temperature is not None:
        print("temperatura je", temperature, "vlaga je", humidity)
    else:
        print("ni bilo mogoče uspostaviti povezave s senzorjem, preverite povezavo")