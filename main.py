from machine import Pin, I2C, SPI
from ssd1306 import SSD1306_I2C
import framebuf
from time import sleep
import uos
#download sdcard from thonny library and formating should be done before using sdcard
import sdcard

# Create oled connection
id = 0
sda = Pin(0)
scl = Pin(1)
i2c = I2C(id=id, scl=scl, sda=sda)
oled = SSD1306_I2C(width=128, height=64, i2c=i2c)

# SD card setup
cs = Pin(13, Pin.OUT)
spi = SPI(1, sck=Pin(14), mosi=Pin(15), miso=Pin(12))
sd = sdcard.SDCard(spi, cs)


#check if you mounted the sd card
try:
    uos.mount(sd, '/sd')
    print("SD card mounted successfully.", uos.listdir("/sd/"))
except OSError as e:
    print("Failed to mount SD card:", e)


# Set file path
file_path = '/sd/bh_pbm_converted'

for file_name in uos.listdir(file_path):
    #Only selects images ending in pbm
    if file_name.endswith(".pbm"):
        #Joins the path '/sd/bh_pbm_converted' and "BlvckHvrts0000.pbm" together
        file_path_full = "/".join([file_path, file_name])
        #opens the pbm file
        with open(file_path_full, 'rb') as f:
            #read through the first two lines in order read the bytearray
            f.readline()
            f.readline()
            #create bytearray with pbm data
            data = bytearray(f.read())
        #create frame buffer with data
        fbuf = framebuf.FrameBuffer(data, 128, 64, framebuf.MONO_HLSB)
        #display frame
        oled.invert(1)
        oled.blit(fbuf, 0, 0)
        oled.show()
    else:
        print("Skipping non-PBM file:", file_name)
# screen diplay off        
oled.off()

   



