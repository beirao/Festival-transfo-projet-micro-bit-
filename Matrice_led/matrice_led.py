# Add your Python code here. E.g.
from microbit import *



while True :

    
    inclinaison = accelerometer.get_x()
    
    if button_a.is_pressed() and (inclinaison > 200 or inclinaison <-200):
        emoji_content = Image("00000:"
                              "09990:"
                              "00000:"
                              "09990:"
                              "90009")
        
        display.show(emoji_content)
        sleep(1500)
    
    elif button_a.is_pressed():
        emoji_content = Image("05050:"  #display.show(Image.HAPPY)
                              "09090:"
                              "00000:"
                              "90009:"
                              "09990")
        
        display.show(emoji_content)
        sleep(100)
                              
        emoji_content = Image("05000:"
                              "09050:"
                              "00000:"
                              "90009:"
                              "09990")
        
        display.show(emoji_content)
        sleep(100)
    

    else :
        display.clear()
        
    #---------------
    
    inclinaison = accelerometer.get_x()
    if inclinaison > 20:
        display.show("D")
    elif inclinaison < -20:
        display.show("G")
    else:
        display.show("-")
