import Adafruit_DHT

DHT_SENSOR = Adafruit_DHT.DHT11
DHT_PIN = 4
print(" ˙C    I    vlaga%")
while True:
    humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)

    if humidity is not None and temperature is not None:
        if humidity is 90:
            print("vlaga je zelo visoka")
        else:
            print("")
        print(int(temperature), "    I    ", int(humidity))
    else:
        print("ni bilo mogoče uspostaviti povezave s senzorjem, preverite povezavo")
        print("to ni bilo mogoce")
