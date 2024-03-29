import RPi.GPIO as GPIO
import time
import board
import neopixel
import random

GPIO.setmode(GPIO.BCM)

pixels = neopixel.NeoPixel(board.D21, 5)

def initialize(trig, echo):
        # trig = 26
        # echo = 19
        GPIO.setup(trig, GPIO.OUT)
        GPIO.setup(echo, GPIO.IN)

def distance(trig, echo):
        
        GPIO.output(trig, 1)#zapiskamo        
        time.sleep(0.00001)#počakamo 0.01ms
        GPIO.output(trig, 0) #nehamo piskat

        zacetniCas = time.time()
        koncniCas = time.time()


        while GPIO.input(echo) == 0: #čakamo dokler je tišina
                zacetniCas = time.time() #zapišemo si zadnji čas ko je tišina
        
        while GPIO.input(echo) == 1: #čakamo dokler slišimo pisk
                koncniCas = time.time() #zapišemo si čas konca piska
        
        razlikaCas = koncniCas - zacetniCas

        razdalja = (razlikaCas * 34200) / 2 #izračunamo razdaljo, delimo z dve ker zvok prepotuje dvojno pot do ovire

        #print("V spremenljivki __name__ se skriva", __name__)
        return razdalja


r = random.randint(0,255)
g = random.randint(0,255)
b = random.randint(0,255)

if __name__ == "__main__": #izvajamo skripto uzSenzor
        try:
                trig = 26
                echo = 19
                initialize(trig, echo)
                while True:
                        razd = distance(trig, echo)
                        print("Izmerjena razdalja je", razd, "cm.")
                        if razd >= 15:
                            pixels[0] = (0,0,0)
                            pixels[1] = (0,0,0)
                            pixels[2] = (0,0,0)
                            pixels[3] = (0,0,0)
                            pixels[4] = (0,0,0)
                        if razd <= 15.9 and razd >= 13:
                            pixels[0] = (0,255,0)
                            pixels[1] = (0,0,0)
                            pixels[2] = (0,0,0)
                            pixels[3] = (0,0,0)
                            pixels[4] = (0,0,0)
                        if razd <= 12.9 and razd >= 11:
                            pixels[0] = (220,255,0)
                            pixels[1] = (220,255,0)
                            pixels[2] = (0,0,0)
                            pixels[3] = (0,0,0)
                            pixels[4] = (0,0,0)
                        if razd <= 10.9 and razd >= 9:
                            pixels[0] = (255,200,0)
                            pixels[1] = (255,200,0)
                            pixels[2] = (255,200,0)
                            pixels[3] = (0,0,0)
                            pixels[4] = (0,0,0)
                        if razd <= 8.9 and razd >= 7:
                            pixels[0] = (255,120,0)
                            pixels[1] = (255,120,0)
                            pixels[2] = (255,120,0)
                            pixels[3] = (255,120,0)
                            pixels[4] = (0,0,0)
                        if razd <= 6.9:
                            r = random.randint(0,255)
                            g = random.randint(0,255)
                            b = random.randint(0,255)
                            k = random.randint(1,3)
                            if k == 1:
                                r = 0
                            if k == 2:
                                g = 0
                            if k == 3:
                                b = 0
                            pixels[0] = (r,g,b)
                            r = random.randint(0,255)
                            g = random.randint(0,255)
                            b = random.randint(0,255)
                            k = random.randint(1,3)
                            if k == 1:
                                r = 0
                            if k == 2:
                                g = 0
                            if k == 3:
                                b = 0
                            pixels[1] = (r,g,b)
                            r = random.randint(0,255)
                            g = random.randint(0,255)
                            b = random.randint(0,255)
                            k = random.randint(1,3)
                            if k == 1:
                                r = 0
                            if k == 2:
                                g = 0
                            if k == 3:
                                b = 0
                            pixels[2] = (r,g,b)
                            r = random.randint(0,255)
                            g = random.randint(0,255)
                            b = random.randint(0,255)
                            k = random.randint(1,3)
                            if k == 1:
                                r = 0
                            if k == 2:
                                g = 0
                            if k == 3:
                                b = 0
                            pixels[3] = (r,g,b)
                            r = random.randint(0,255)
                            g = random.randint(0,255)
                            b = random.randint(0,255)
                            k = random.randint(1,3)
                            if k == 1:
                                r = 0
                            if k == 2:
                                g = 0
                            if k == 3:
                                b = 0
                            pixels[4] = (r,g,b)
                    
                    
                        time.sleep(0.5)
        except KeyboardInterrupt:
                print("Uporabnik je pritisnil ctrl + c.")
                GPIO.cleanup()
