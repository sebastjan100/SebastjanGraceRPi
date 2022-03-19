import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

def initialize(trig, echo):
    #trig = 26
    #echo = 24
    GPIO.setup(trig, GPIO.OUT)
    GPIO.setup(echo, GPIO.IN)

def distance(trig, echo):
    GPIO.output(trig, GPIO.HIGH)#GPIO.HIGH = 1 = True
    time.sleep(0.00001)
    GPIO.output(trig, GPIO.LOW)#GPIO.HIGH = 0 = False

    start_time = time.time()#time in seconds from 1.1.1970
    final_time = time.time()
    timeout_time = time.time()

    while GPIO.input(echo) == 0:
        start_time = time.time()
        if start_time - timeout_time >= 3:
            return "Error recieving nothing."
            break
    
    while GPIO.input(echo) == 1:
        final_time = time.time()
    
    distance = (final_time - start_time) / 2 * 34200#sound travels 342m in a second
    #print("__name__:", __name__)
    return distance

if __name__ == "__main__":
    #running ultra_sonic_sensor.py script
    try:
        trig = 26
        echo = 19
        initialize(trig, echo)
        while True:
            distance = int(distance(trig, echo))
            print("Measured distance: %.1f cm." % distance)

            time.sleep(2)
    except KeyboardInterrupt:
        print("Ctrl-c pressed --> exiting.")
        GPIO.cleanup()
