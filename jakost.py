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

        if clkState == 0 and dtState == 1 and dc < 96:#if dt's state is 1 and clk's state is 0 that means that dt is infront of clk and so we are moving clockwise
                dc += 5
 
def dtClicked(channel):
        global dc
        #Premikamo se v smeri urinega kazalca, če je pin 17 == 1 in pin 18 == 0
        clkState = GPIO.input(clk)
        dtState = GPIO.input(dt)

        if clkState == 1 and dtState == 0 and dc > 4:
                dc -= 5

GPIO.add_event_detect(clk, GPIO.FALLING, callback=clkClicked, bouncetime=20)
GPIO.add_event_detect(dt, GPIO.FALLING, callback=dtClicked, bouncetime=20)

# main loop of program
print("\nPress Ctl C to quit \n")  # Print blank line before and after message.
pwm.start(dc)                      # Start PWM with 0% duty cycle

try:
    while True:                      # Loop until Ctl C is pressed to stop.
        pwm.ChangeDutyCycle(dc)
        time.sleep(0.05)             # wait .05 seconds at current LED brightness
        print(dc)
except KeyboardInterrupt:
    print("Ctl C pressed - ending program")

pwm.stop()                         # stop PWM
GPIO.cleanup()                     # resets GPIO ports used back to input mode