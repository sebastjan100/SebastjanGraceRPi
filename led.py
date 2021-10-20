import RPi.GPIO as GPIO
import time


GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

rdeca = 22

GPIO.setup(rdeca,GPIO.OUT)

while True:
        print ("LED on")
        GPIO.output(rdeca,GPIO.HIGH)
        time.sleep(1.5)
        print ("LED off")
        GPIO.output(rdeca,GPIO.LOW)
        time.sleep(0.5)
        print ("LED on")
        GPIO.output(rdeca,GPIO.HIGH)
        time.sleep(0.5)
        print ("LED off")
        GPIO.output(rdeca,GPIO.LOW)
        time.sleep(0.5)
        print ("LED on")
        GPIO.output(rdeca,GPIO.HIGH)
        time.sleep(0.5)
        print ("LED off")
        GPIO.output(rdeca,GPIO.LOW)
        time.sleep(0.5)
        print ("LED on")
        GPIO.output(rdeca,GPIO.HIGH)
        time.sleep(1.5)
        print ("LED off")
        GPIO.output(rdeca,GPIO.LOW)
        time.sleep(0.5)
        print ("LED on")
        GPIO.output(rdeca,GPIO.HIGH)
        time.sleep(0.5)
        print ("LED off")
        GPIO.output(rdeca,GPIO.LOW)
        time.sleep(0.5)
        print ("LED on")
        GPIO.output(rdeca,GPIO.HIGH)
        time.sleep(0.5)
        GPIO.output(rdeca,GPIO.LOW)
        print ("LED off")
        time.sleep(0.5)
        