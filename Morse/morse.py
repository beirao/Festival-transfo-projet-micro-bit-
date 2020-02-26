
import radio
from microbit import *

display.show("K")


flash = Image("99999:"
              "99999:"
              "99999:"
              "99999:"
              "99999")


radio.on()

while True:
    if button_a.was_pressed():
        radio.send('flash')  # a-ha
    incoming = radio.receive()
    if incoming == 'flash':
        
        display.show(flash, delay=100)
        sleep(100)
        display.clear()
