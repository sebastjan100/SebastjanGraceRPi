import Adafruit_DHT
DHT_SENSOR = Adafruit_DHT.DHT11
DHT_PIN = 4
while True:
    humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)

    try:
        if humidity is not None and temperature is not None:
            print("Temperatura je", temperature, "vlaga pa znaša", humidity)
        else:
            print("ni bilo mogoče uspostaviti povezave s senzorjem, preverite povezavo")
            print("to ni bilo mogoce")
    except KeyboardInterrupt:
        print("Uporabnik je pritisnil ctrl + c")