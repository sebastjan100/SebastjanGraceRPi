import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

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

        razdalja = (razlikaCas * 34200)/2 #izračunamo razdaljo, delimo z dve ker zvok prepotuje dvojno pot do ovire

        #print("V spremenljivki __name__ se skriva", __name__)
        return razdalja

if __name__ == "__main__": #izvajamo skripto uzSenzor
        try:
                trig = 26
                echo = 19
                initialize(trig, echo)
                while True:
                        razd = distance(trig, echo)
                        print("Izmerjena razdalja je", float(razd, 3), "cm.")
                        time.sleep(2)
        except KeyboardInterrupt:
                print("Uporabnik je pritisnil ctrl + c.")
                GPIO.cleanup()
