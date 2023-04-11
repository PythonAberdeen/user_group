from machine import Pin, I2C
from time import sleep
from ht16k33 import ht16k33_seg

button = Pin(5, Pin.IN)

prev = 0
i2c = I2C(sda=Pin(18), scl=Pin(19), freq=100000)
d = ht16k33_seg.Seg7x4(i2c)
i = 0

while True:
    cur = button.value()
    d.text("{:04d}".format(i))
    d.show() 
    
    if cur != prev:
        if cur:
            print("Pressed")
            sleep(5)
        else:
            print("Released")
            i = 0
        prev = cur
    i += 1  
    sleep(1)
        
