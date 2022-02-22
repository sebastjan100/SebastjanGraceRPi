import RPi.GPIO as GPIO
import time
import uzSenzor as UZ

trig = 26
print(trig)
echo = 19
print(echo)

try: 
    UZ.initialize(26, 19)
    while True:
        razd = UZ.distance(trig, echo)
        print("Izmerjena razdalja je", razd, "cm.")
        time.sleep(2)
except KeyboardInterrupt:
    print("Uporabnik je pritisnil ctrl + c.")
    GPIO.cleanup()