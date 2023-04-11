from machine import Pin, I2C
from time import sleep
from ht16k33 import ht16k33_seg

i2c = I2C(sda=Pin(18), scl=Pin(19), freq=100000)

d = ht16k33_seg.Seg7x4(i2c)

while True:
    for i in range(10):
        d.push(str(i))
        d.show()
        sleep(1)
