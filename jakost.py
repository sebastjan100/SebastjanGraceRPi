from RPi import GPIO
import time

rdeca = 22

step = 5 #shranimo korak, ki ga pristejemo ali odstejejo, ko se zavrti enkoder
paused = False #spremljamo stanje, kdaj se ustavimo

#povemo kako bomo nastavili GPIO pine; uporabljamo logicni nacin, to kar je napisano na GPIO clenu
GPIO.setmode(GPIO.BCM)

#clk in st sta spremenjlivki, ki povesta kam smo povezali pina (s1, s2)
#sw je spremenjivka, ki pove kam je povezana tipka(key)
clk = 17
dt = 18
sw = 27

#nastavimo vhodne in izhodne enote
#GPIO.setup(pin, vhod/izhod, nacin)
GPIO.setup(clk, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(dt, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(sw, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

#preverimo in nastavimo prvotno stanje
counter = 0#stevec zacne steti s 0
clkLastState = GPIO.input(clk)#preberemo stanje na pinu 17
dtLastState = GPIO.input(dt)#preberemo stanje na pinu 18
swLastState = GPIO.input(sw)#preberemo stanje na pinu 27 - key

#define functions which will be triggered on pin state changes
def clkClicked(channel):
        global counter#uporabimo globalni spremenjivko counter
        global step#uporabimo globalni spremenjivko step

        clkState = GPIO.input(clk)
        dtState = GPIO.input(dt)
        if clkState == 0 and dtState == 1:
                counter = counter + step
                print ("Counter ", counter)

def dtClicked(channel):
        global counter
        global step

        clkState = GPIO.input(clk)
        dtState = GPIO.input(dt)
        
        if clkState == 1 and dtState == 0:
                counter = counter - step
                print ("Counter ", counter)


def swClicked(channel):
        global paused
        paused = not paused



GPIO.add_event_detect(clk, GPIO.FALLING, callback=clkClicked, bouncetime=50)
GPIO.add_event_detect(dt, GPIO.FALLING, callback=dtClicked, bouncetime=50)
GPIO.add_event_detect(sw, GPIO.FALLING, callback=swClicked, bouncetime=50)

input("Start monitoring input")


if counter >= 100:
        counter = 100

if counter <= 0:
        counter = 0

GPIO.setup(rdeca, GPIO.OUT)
pwm = GPIO.PWM(rdeca, 100)

pwm.start(counter)
pwm.ChangeDutyCycle(counter)
print(counter)
print("\nCtl C pressed - ending program")

pwm.stop()                         # stop PWM
GPIO.cleanup()                     # resets GPIO ports used back to input mode