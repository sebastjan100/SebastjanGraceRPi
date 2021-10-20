from RPi import GPIO

rdeca = 22

step = 5
paused = False 

GPIO.setmode(GPIO.BCM)
GPIO.setup(rdeca, GPIO.OUT)
pwm = GPIO.PWM(rdeca, 100)

clk = 17
dt = 18
sw = 27
counter = 0

pwm.start(counter)

GPIO.setup(clk, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(dt, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(sw, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)



clkLastState = GPIO.input(clk)
dtLastState = GPIO.input(dt)
swLastState = GPIO.input(sw)

def clkClicked(channel):
        global counter
        global step

        clkState = GPIO.input(clk)
        dtState = GPIO.input(dt)
        if clkState == 0 and dtState == 1:
                counter = counter + step
                pwm.ChangeDutyCycle(counter)
                print ("Counter ", counter)

def dtClicked(channel):
        global counter
        global step

        clkState = GPIO.input(clk)
        dtState = GPIO.input(dt)
        
        if clkState == 1 and dtState == 0:
                counter = counter - step
                pwm.ChangeDutyCycle(counter)
                print ("Counter ", counter)


def swClicked(channel):
        global paused
        paused = not paused



GPIO.add_event_detect(clk, GPIO.FALLING, callback=clkClicked, bouncetime=50)
GPIO.add_event_detect(dt, GPIO.FALLING, callback=dtClicked, bouncetime=50)
GPIO.add_event_detect(sw, GPIO.FALLING, callback=swClicked, bouncetime=50)

input("Start monitoring input")


if counter >= 100:
        counter -= 5
        print("deluje 1")

if counter <= 0:
        counter += 5
        print("deluje 2")

print("\nCtl C pressed - ending program")

pwm.stop()
GPIO.cleanup()