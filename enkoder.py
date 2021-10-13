#uvozimo knjiznico za delo z GPIO pini
from RPi import GPIO


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

        clkState = GPIO.input(clk)#preberemo stanje na pinu 17
        dtState = GPIO.input(dt)#preberemo stanje na pinu 18

        #premikamo se v smeri urinega kazalca, ce je pin 17 == 0 in pin 18 == 1
        if clkState == 0 and dtState == 1:
                #pristejemo korak - vrtimo se v smeri urinega kazalca
                counter = counter + step
                print ("Counter ", counter)

def dtClicked(channel):
        global counter
        global step

        clkState = GPIO.input(clk)
        dtState = GPIO.input(dt)
        
        #premikamo se v obratni smeri urinega kazalca, ce je pin 18 == 0 in pin 17 == 1
        if clkState == 1 and dtState == 0:
                #odstejemo korak - vrtimo se v obratni smeri urinega kazalca
                counter = counter - step
                print("Counter ", counter)


def swClicked(channel):
        global paused#povemo da bomo uporabili gllobalno spremenjivko
        paused = not paused#obrnemo vrednost spremenjivke poused
        print ("Paused ", paused)

#na zacetku sprintamo zacetno staje
print ("Initial clk:", clkLastState)
print ("Initial dt:", dtLastState)
print ("Initial sw:", swLastState)
print ("=========================================")

#nastavimo prekinitve
#GPIO.add_event_detect(pin, kdaj preberemo FALLING/RISING/ONCHANGE, katero funkcijo naj izvede, nastavimo koliko casa naj prekinitev pocaka pred ponovno izvedbo)
GPIO.add_event_detect(clk, GPIO.FALLING, callback=clkClicked, bouncetime=50)
GPIO.add_event_detect(dt, GPIO.FALLING, callback=dtClicked, bouncetime=50)
GPIO.add_event_detect(sw, GPIO.FALLING, callback=swClicked, bouncetime=50)

input("Start monitoring input")

#pocistimo nastavitve vseh pinov
GPIO.cleanup()
