import RPi.GPIO as GPIO
import Adafruit_DHT
import time
#####dht
import vlaga as DHT

#####uz
import uzSenzor as US

#####oled ekran
#import Adafruit_GPIO.SPI as SPI
import Adafruit_SSD1306

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

import subprocess

import uzSenzor as UZ

RST = None     # on the PiOLED this pin isnt used
# Note the following are only used with SPI:
DC = 23
SPI_PORT = 0
SPI_DEVICE = 0

disp = Adafruit_SSD1306.SSD1306_128_32(rst=RST)

#####dht
DHT_SENSOR = Adafruit_DHT.DHT11

#####uz senzor
trig = 26
print(trig)
echo = 19
print(echo)

# Initialize library.
disp.begin()

# Clear display.
disp.clear()
disp.display()

width = disp.width
height = disp.height

image = Image.new('1', (width, height))

# Get drawing object to draw on image.
draw = ImageDraw.Draw(image)
draw.rectangle((0,0,width,height), outline=0, fill=0)

# Draw some shapes.
# First define some constants to allow easy resizing of shapes.
padding = -2
top = padding
bottom = height-padding
# Move left to right keeping track of the current x position for drawing shapes.
x = 0


# Load default font.
font = ImageFont.load_default()

try:
    trig = 26
    echo = 19
    US.initialize(trig, echo)
    
    dht_pin = 4
    DHT.setDHT_pin(dht_pin)
    while True:
        # Draw a black filled box to clear the image.
        draw.rectangle((0,0,width,height), outline=0, fill=0)
    
        cmd = "hostname -I | cut -d\' \' -f1"
    
        IP = subprocess.check_output(cmd, shell = True )
        razd = US.distance(trig, echo)
        humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR, dht_pin)
    
        # Write two lines of text.
        draw.text((x, top),       "IP: " + str(IP),  font=font, fill=255)
        draw.text((x, top + 8),     "razd: " + str(razd), font=font, fill=255)
        draw.text((x, top + 16),    "hum: " + str(humidity),  font=font, fill=255)
        draw.text((x, top + 25),    "temp: " + str(temperature),  font=font, fill=255)
    
        # Display image.
        disp.image(image)
        disp.display()
        time.sleep(2)

except KeyboardInterrupt:
    print("Uporabnik je pritisnil ctrl + c.")
    draw.rectangle((0,0,width,height), outline=0, fill=0)
    disp.display()
    GPIO.cleanup()
