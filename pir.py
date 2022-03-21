import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
PIR_PIN = 13
GPIO.setup(PIR_PIN, GPIO.IN)
x = 0

try:
    print ("PIR Module Test (CTRL+C to exit)")
    time.sleep(2)
    print("Ready")
    while True:
        if GPIO.input(PIR_PIN):
            x += 1
            print ("Detected " + str(x) + " motion")
        time.sleep(0)
except KeyboardInterrupt:
    print ("Quit")
    GPIO.cleanup()

