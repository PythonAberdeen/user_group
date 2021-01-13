from machine import Pin, I2C
from time import sleep
import dht
from ht16k33 import ht16k33_seg

sensor = dht.DHT11(Pin(26))
i2c = I2C(sda=Pin(18), scl=Pin(19), freq=100000)
d = ht16k33_seg.Seg7x4(i2c)
button = Pin(5, Pin.IN)
toggle = True

while True:
  if button.value():
    toggle = not toggle
    print("Toggle: ", toggle)
  try:
    sensor.measure()
    if toggle:
      output = sensor.temperature()
    else:
      output = sensor.humidity()
    d.fill(0)
    d.number(output)
    d.show()
    sleep(2)

  except OSError as e:
    print('Failed to read sensor.')
