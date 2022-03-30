import RPi.GPIO as GPIO
import time
import board
import neopixel
GPIO.setmode(GPIO.BCM)


pixel_pin = board.D21

num_pixels = 5

ORDER = neopixel.GRB

pixels = neopixel.NeoPixel(
    pixel_pin, num_pixels, brightness=0.2, auto_write=False, pixel_order=ORDER
)

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





def wheel(pos):
    # Input a value 0 to 255 to get a color value.
    # The colours are a transition r - g - b - back to r.
    if pos < 0 or pos > 255:
        r = g = b = 0
    elif pos < 85:
        r = int(pos * 3)
        g = int(255 - pos * 3)
        b = 0
    elif pos < 170:
        pos -= 85
        r = int(255 - pos * 3)
        g = 0
        b = int(pos * 3)
    else:
        pos -= 170
        r = 0
        g = int(pos * 3)
        b = int(255 - pos * 3)
    return (r, g, b) if ORDER in (neopixel.RGB, neopixel.GRB) else (r, g, b, 0)



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
                            for j in range(255):
                                for i in range(num_pixels):
                                    pixel_index = (i * 256 // num_pixels) + j
                                    pixels[i] = wheel(pixel_index & 255)
                                pixels.show()
                            
                        time.sleep(0.1)
        except KeyboardInterrupt:
                print("Uporabnik je pritisnil ctrl + c.")
                GPIO.cleanup()





