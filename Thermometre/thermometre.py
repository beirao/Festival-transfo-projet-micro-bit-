# Add your Python code here. E.g.
from microbit import *

tempinit = 0

while True:
    temp = temperature()
    
    if button_a.is_pressed() :
        display.scroll(temp)
    
    if (tempinit+temp)<=5 :
        jauge = Image("00000:"
                      "00000:"
                      "00000:"
                      "00000:"
                      "55555")
                      
    elif (tempinit+temp)>5 and (tempinit+temp)<=10 :
        jauge = Image("00000:"
                      "00000:"
                      "00000:"
                      "00000:"
                      "99999")
                      
    elif (tempinit+temp)>10 and (tempinit+temp)<=15 :
        jauge = Image("00000:"
                      "00000:"
                      "00000:"
                      "55555:"
                      "99999")
    
    elif (tempinit+temp)>15 and (tempinit+temp)<=20 :
        jauge = Image("00000:"
                      "00000:"
                      "00000:"
                      "99999:"
                      "99999")
                              
    elif (tempinit+temp)>20 and (tempinit+temp)<=25 :
        jauge = Image("00000:"
                      "00000:"
                      "55555:"
                      "99999:"
                      "99999")   

    elif (tempinit+temp)>25 and (tempinit+temp)<=30 :
        jauge = Image("00000:"
                      "00000:"
                      "99999:"
                      "99999:"
                      "99999")
                              
    elif (tempinit+temp)>30 and (tempinit+temp)<=35 :
        jauge = Image("00000:"
                      "55555:"
                      "99999:"
                      "99999:"
                      "99999")                              
                              
    elif (tempinit+temp)>35 and (tempinit+temp)<=40 :
        jauge = Image("00000:"
                      "99999:"
                      "99999:"
                      "99999:"
                      "99999")   
                              
    elif (tempinit+temp)>40 and (tempinit+temp)<=45 :
        jauge = Image("55555:"
                      "99999:"
                      "99999:"
                      "99999:"
                      "99999")  
    else :
        jauge = Image("99999:"
                      "99999:"
                      "99999:"
                      "99999:"
                       "99999")
  
    display.show(jauge)
