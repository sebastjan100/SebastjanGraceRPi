import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

trig = 26
echo = 24

GPIO.setup(trig, GPIO.OUT)
GPIO.setup(echo, GPIO.IN)

def distance():

        GPIO.output(trig, 1)#zapiskamo
        time.sleep(0.00001)#pocakamo  0.01ms
        GPIO.output(trig, 0)#nehamo piskat

        zacetniCas = time.time()
        koncniCas = time.time()

        while GPIO.input(echo) == 0:#cakamo dokler je tisina
                zacetniCas = time.time()#zapisemo si zadnji cas ko je tisina

        while GPIO.input(echo) == 1:#cakamo dokler slisimo pisk
                koncniCas = time.time()#zapisemo si cas konca piska

        razlikaCas = koncniCas - zacetniCas
        
        razdalja = (razlikaCas * 34200)/2#izracujnamo razdaljo, delimo z dve ker zvok prepotuje dvojno pot do ovire

        print("v spremenjivki __name__ se skriva", __name__)
        return razdalja

if __name__ == "__main__":# izvajamo skripto uzSenzor
        try:
                while True:
                        razd = distance()
                        print("izmerjena razdalja je", razd, "cm.")
                        time.sleep(2)
        except KeyboardInterrupt:
                print("Uporabnik je pritisnil ctrl + c")
                GPIO.cleanup
