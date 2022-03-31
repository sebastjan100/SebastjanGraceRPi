import RPi.GPIO as GPIO
import ultra_sonic_sensor as US
import dht as DHT
import send
import pir as PIR
import encoder as ENC
import Adafruit_GPIO.SPI as SPI
import Adafruit_SSD1306, time, subprocess
from PIL import Image, ImageDraw, ImageFont

RST = None
DC = 23
SPI_PORT = 0
SPI_DEVICE = 0

url = "https://gracewebapp-sebastjantekavc.online404.repl.co/"
apiKey = "sebastjan"

disp = Adafruit_SSD1306.SSD1306_128_32(rst=RST)
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

try:
    trig = 26
    echo = 19
    US.initialize(trig, echo)

    dht_pin = 4
    DHT.setDHT_pin(dht_pin)

    pir_pin = 13
    PIR.pir_setup(pir_pin)

    clk = 17
    dt = 5
    sw = 27
    ENC.setENC_pin(clk, dt, sw)
    while True:
        draw.rectangle((0,0,width,height), outline=0, fill=0)

        click = ENC.getClicked()
        draw.text((x, top), "Clicked: " + str(click),  font=font, fill=255)

        distance = US.calculate_distance()
        #print("Measured distance: %.1f cm." % distance)
        draw.text((x, top+8), "Distance: " + str("%.1f" % distance) + "cm", font=font, fill=255)
        send.sendUS(distance, url, "api/uss", apiKey)

        data = DHT.get_humidity()
        draw.text((x, top+16), "Humidity: " + str(data[0]) + "%", font=font, fill=255)
        draw.text((x, top+24), "Temperature: " + str(data[1]) + "Â°C", font=font, fill=255)
        send.sendDHT(data, url, "api/dht", apiKey)

        if PIR.detect_motion():
            send.sendPIR(url, "api/pir", apiKey)

        print("Batch of requests sent!\n")
        
        disp.image(image)
        disp.display()

        time.sleep(2)
except KeyboardInterrupt:
    print("Ctrl+c pressed --> exiting.")
    draw.rectangle((0,0,width,height), outline=0, fill=0)
    disp.image(image)
    disp.display()
    GPIO.cleanup()