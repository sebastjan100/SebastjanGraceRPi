import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(22,GPIO.OUT)
print "LED on"
GPIO.output(22,GPIO.HIGH)
time.sleep(0.5)
print "LED off"
GPIO.output(22,GPIO.LOW)
time.sleep(0.5)
print "LED on"
GPIO.output(22,GPIO.HIGH)
time.sleep(0.5)
print "LED off"
GPIO.output(22,GPIO.LOW)
time.sleep(0.5)
print "LED on"
GPIO.output(22,GPIO.HIGH)
time.sleep(0.5)
print "LED off"
GPIO.output(22,GPIO.LOW)
time.sleep(1.5)
print "LED on"
GPIO.output(22,GPIO.HIGH)
time.sleep(0.5)
print "LED off"
GPIO.output(22,GPIO.LOW)
time.sleep(0.5)
print "LED on"
GPIO.output(22,GPIO.HIGH)
time.sleep(0.5)
print "LED off"
GPIO.output(22,GPIO.LOW)
time.sleep(0.5)
print "LED on"
GPIO.output(22,GPIO.HIGH)
time.sleep(0.5)
print "LED off"
GPIO.output(22,GPIO.LOW)
time.sleep(1.5)
print "LED on"
GPIO.output(22,GPIO.HIGH)
time.sleep(0.5)
print "LED off"
GPIO.output(22,GPIO.LOW)

