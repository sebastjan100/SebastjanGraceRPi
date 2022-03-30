import RPi.GPIO as GPIO
import time

import uzSenzor as UZ
import vlaga as DHT
import poslji

import Adafruit_SSD1306

from PIL import Image, ImageDraw, ImageFont

import subprocess

# Raspberry Pi pin configuration:
RST = None     # on the PiOLED this pin isnt used

# 128x32 display with hardware I2C:
disp = Adafruit_SSD1306.SSD1306_128_32(rst=RST)

# web app data
url = "https://GraceWebApp-SebastjanTekavc.online404.repl.co"
apikey = "sebastjan"

# Initialize library.
disp.begin()

# Clear display.
disp.clear()
disp.display()

# Create blank image for drawing.
# Make sure to create image with mode '1' for 1-bit color.
width = disp.width
height = disp.height
image = Image.new('1', (width, height))

# Get drawing object to draw on image.
draw = ImageDraw.Draw(image)

# Draw a black filled box to clear the image.
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


trig = 26
echo = 19


UZ.initialize(trig, echo) 

dht_pin = 4
DHT.setDHT_pin(dht_pin)

try: 
        while True:
                draw.rectangle((0,0,width,height), outline=0, fill=0)

                cmd = "hostname -I | cut -d\' \' -f1"
                IP = subprocess.check_output(cmd, shell = True )
                draw.text((x, top),       "IP: " + str(IP),  font=font, fill=255)

                razd = UZ.distance(trig, echo)
                print("Izmerjena razdalja je", razd, "cm.")
                draw.text((x, top+8),  "Razdalja:" + str(round(razd,2)) + " cm", font=font, fill=255)
                poslji.posljiUZ(razd, url, "/api/uz/", apikey)

                data = DHT.get_humidity()
                print("Vlaga", data[0], "temp", data[1])
                draw.text((x, top+8),  "HUM:" + str(data[0]) + " %", font=font, fill=255)
                draw.text((x, top+8),  "TEMP:" + str(data[1]) + " cm", font=font, fill=255)
                poslji.posljiDHT(data, url, "/api/dht/", apikey)

                disp.image(image)
                disp.display()
                time.sleep(1)
except KeyboardInterrupt:
        print("Uporabnik je pritisnil ctrl + c.")
        GPIO.cleanup()