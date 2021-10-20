import RPi.GPIO as GPIO
import time


GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

rdeca = 22

GPIO.setup(rdeca,GPIO.OUT)

while True:
        print ("LED on")
        GPIO.output(rdeca,GPIO.HIGH)
        time.sleep(0.001)#1 ms
        print ("LED off")
        GPIO.output(rdeca,GPIO.LOW)
        time.sleep(0.008)#8 ms