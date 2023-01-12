from machine import Pin

button = Pin(5, Pin.IN)

prev = 0

while True:
    cur = button.value()
    if cur != prev:
        if cur:
            print("Pressed")
        else:
            print("Released")
        prev=cur
