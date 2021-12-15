#pwm = pulse width modulation
import RPi.GPIO as GPIO   # Import the GPIO library.
import time               # Import time library

GPIO.setmode(GPIO.BCM)  # Set Pi to use pin number when referencing GPIO pins.
# Can use GPIO.setmode(GPIO.BCM) instead to use 
# Broadcom SOC channel names.

led = 22
clk = 17
dt = 18
sw = 27
dc=5# set dc variable to 0 for 0%

GPIO.setup(clk, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(dt, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(sw, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

GPIO.setup(led, GPIO.OUT)  # Set GPIO pin 12 to output mode.
pwm = GPIO.PWM(led, 100)   # Initialize PWM on pwmPin 100Hz frequency

def clkClicked(channel):
        global dc
 
        clkState = GPIO.input(clk)
        dtState = GPIO.input(dt)

        if clkState == 0 and dtState == 1 and dc < 96:
                dc += 5
 
def dtClicked(channel):
        global dc
        clkState = GPIO.input(clk)
        dtState = GPIO.input(dt)

        if clkState == 1 and dtState == 0 and dc > 4:
                dc -= 5

GPIO.add_event_detect(clk, GPIO.FALLING, callback=clkClicked, bouncetime=20)
GPIO.add_event_detect(dt, GPIO.FALLING, callback=dtClicked, bouncetime=20)

# main loop of program
print("\nPress Ctl C to quit \n")
pwm.start(dc)
try:
    while True:  
        pwm.ChangeDutyCycle(dc)
        time.sleep(0.05)
        print(dc)
except KeyboardInterrupt:
    print("\nCtl C pressed - ending program")

pwm.stop() 
GPIO.cleanup() 