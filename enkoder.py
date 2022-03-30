#uvozimo knjiznico za delo z GPIO pini
from RPi import GPIO

#####GLOBALNO!!!!!!!!!!!!!!
counter = 0#stevec zacne steti s 0


step = 5 #shranimo korak, ki ga pristejemo ali odstejejo, ko se zavrti enkoder
paused = False #spremljamo stanje, kdaj se ustavimo

def initialize(clk,dt,sw):

    GPIO.setup(clk, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(dt, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(sw, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    
    #preverimo in nastavimo prvotno stanje
    
    clkLastState = GPIO.input(clk)#preberemo stanje na pinu 17
    dtLastState = GPIO.input(dt)#preberemo stanje na pinu 18
    swLastState = GPIO.input(sw)#preberemo stanje na pinu 27 - key

    print ("Initial clk:", clkLastState)
    print ("Initial dt:", dtLastState)
    print ("Initial sw:", swLastState)
    print ("=========================================")


def clkKlik(clk,dt):
    
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
    return clkClicked

def dtKlik(clk,dt):
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
    return dtClicked


def swClicked(channel):
        global paused#povemo da bomo uporabili gllobalno spremenjivko
        paused = not paused#obrnemo vrednost spremenjivke poused
        print ("Paused ", paused)

defCounter():
    global counter
    return counter

def getClick():
    global paused
    return paused

if __name__ =="__main__":
    clk = 17
    dt = 5
    sw = 27

    initialize(clk, dt, sw)
    
    #nastavimo prekinitve
    #GPIO.add_event_detect(pin, kdaj preberemo FALLING/RISING/ONCHANGE, katero funkcijo naj izvede, nastavimo koliko casa naj prekinitev pocaka pred ponovno izvedbo)
    GPIO.add_event_detect(clk, GPIO.FALLING, callback=clkKlik(clk,dt), bouncetime=50)
    GPIO.add_event_detect(dt, GPIO.FALLING, callback=dtClicked(clk,dt), bouncetime=50)
    GPIO.add_event_detect(sw, GPIO.FALLING, callback=swClicked, bouncetime=50)

input("Start monitoring input")

#pocistimo nastavitve vseh pinov
GPIO.cleanup()
