import Adafruit_DHT

DHT_SENSOR = Adafruit_DHT.DHT11
DHT_PIN = 4

print("TMP [°C] , VLG [%]")

while True:
    humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)

    if humidity is not None and temperature is not None:
        print(temperature, ",",  humidity)
        if humidity >= 90.0:
            print("Zivis v akvariju!")
        if humidity <= 30.0:
            print("Zivis v Sahari!")
    else:
        print("Ups... 404... Ne dela... Preveri povezavo...")
        print("IN se ena stvar... a mas mogoce kaj cipsa?")