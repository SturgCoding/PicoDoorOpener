# Script chooser and handler
from machine import Pin
import ServoMove

def StartUP():
    # When called iterate; disable possible scripts
    i = 1
    while i != 4:
        Handler(i, "off")
        i+=1

def Handler(option, state):
    if option == 1: # Default examplar
        # Toggles the On-Board LED
        LED = Pin('LED', Pin.OUT)
        
        # Case here is to ensure the control remains even after re-connect
        if state == "off":
            LED.low()
        else:
            LED.high()
        return True
     
    # Others will import the related file and allow for better operation
    elif option == 2: 
        # Toggles the Door
        LED = Pin('LED', Pin.OUT)
        
        # Case here is to ensure the control remains even after re-connect
        if state == "off":
            ServoMove.Close()
        else:
            ServoMove.Open()
        return True
    
    elif option == 3:
        pass
    
    print("Value invalid scripts")
    return False
