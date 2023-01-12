from machine import Pin
from neopixel import NeoPixel
from time import sleep

NUM_PIXELS = 14
np = NeoPixel(Pin(16), NUM_PIXELS)
colours = {'red': (255, 0, 0),
           'green': (0, 255, 0),
           'blue': (0, 0, 255),
           'orange': (255, 165, 0),
           'yellow': (255, 255, 0),
           'yel_grn': (255, 255, 0),
           'off': (0,0,0) }

while True:
    np.fill(colours['off'])
    for i in range(7):
        np[i] = colours['yellow']
    np.write()
    sleep(1)
    np.fill(colours['off'])
    for i in range(7, 14):
        np[i] = colours['blue']
    np.write()
    sleep(1)
