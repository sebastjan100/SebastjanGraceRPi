import RPi.GPIO as GPIO
import time

import Adafruit_GPIO.SPI as SPI
import Adafruit_SSD1306
import poslji

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

import subprocess
import valaga as DHT

GPIO.setmode(GPIO.BCM)

RST = None
DC = 23
SPI_PORT = 0
SPI_DEVICE = 0

disp = Adafruit_SSD1306.SSD1306_128_32(rst=RST)

url = "https://gracewebapp-sebastjantekavc.online404.repl.co/"
apikey = "sebastjan"

disp.begin()

disp.clear()
disp.display()

width = disp.width
height = disp.height
image = Image.new('1', (width, height))

draw = ImageDraw.Draw(image)

draw.rectangle((0,0,width,height), outline=0, fill=0)
padding = -2
top = padding
bottom = height-padding
x = 0

font = ImageFont.load_default()

def initialize(trig, echo):
    #trig = 26
    #echo = 19
    GPIO.setup(trig, GPIO.OUT)
    GPIO.setup(echo, GPIO.IN)

def distance(trig, echo):

    GPIO.output(trig, 1) #zapiskamo
    time.sleep(0.00001) #počakamo 0.01ms
    GPIO.output(trig, 0) #nehamo piskati

    zacetniCas = time.time()
    koncniCas = time.time()

    while GPIO.input(echo) == 0: #čakamo dokler je tišina
        zacetniCas = time.time()

    while GPIO.input(echo) == 1: #čakamo dokler slišimo pisk
        koncniCas = time.time()

    razlikaCas = koncniCas - zacetniCas

    razdalja = (razlikaCas * 34315)/2 #centimetri

    print("V spremenljivki __name__ se nahaja", __name__)
    return razdalja


try:
    trig = 26
    echo = 19
    initialize(trig, echo)
    dht_pin = 4
    DHT.setDHT_pin(dht_pin)
    while True:
        draw.rectangle((0,0,width,height), outline=0, fill=0)

        cmd = "hostname -I | cut -d\' \' -f1"
        IP = subprocess.check_output(cmd, shell = True )
        draw.text((x, top),       "IP: " + str(IP),  font=font, fill=255)
        
        razd = distance(trig, echo)
        print("Izmerjena razdalja je", razd, "cm.")
        poslji.posljiUZ(razd, url, "/api/uz/", apikey)

        data = DHT.get_humidity()
        draw.text((x, top+16),    "Humidity: " + str(data[0]) + "%",  font=font, fill=255)
        draw.text((x, top+24),    "Temperature: " + str(data[1]) + "°C",  font=font, fill=255)
        poslji.posljiDHT(data, url, "/api/dht/", apikey)

        disp.image(image)
        disp.display()
        time.sleep(2)
        
except KeyboardInterrupt:
    print("Ctrl + C pritisnjen")
    GPIO.cleanup
