# Add your Python code here. E.g.
from microbit import *
import radio

radio.on()
allume = True
sleep(1000)

while True:
    message = radio.receive()
    
        
    if  message == "ici" :
        radio.send("pret")
        allume = False
        display.show("R") # "R" comme recepteur
        sleep(3000)
        
        while True : #boucle infinie du microbit qui recoit les ordres                                 
            position = radio.receive()
            if position == "rouge":
                display.show(Image("90009:"
                                   "09090:"
                                   "00900:"
                                   "09090:"
                                   "90009"))
            elif position == "vert":
                display.show(Image("00900:"
                                   "09990:"
                                   "00900:"
                                   "00900:"
                                   "00900"))
                
    elif allume :
        radio.send("ici")
        display.show("w")
        if message == "pret" :
                allume = False
    
    else :  
        display.show("E") # "E" comme emetteur 
        sleep(3000)
        
        while True : #boucle infinie du microbit qui donne les ordres
            radio.send("vert")
            display.show(Image("90009:"
                               "09090:"
                               "00900:"
                               "09090:"
                               "90009"))
            sleep(3000)
            radio.send("rouge")
            display.show(Image("00900:"
                               "09990:"
                               "00900:"
                               "00900:"
                               "00900"))
            sleep(3000)
