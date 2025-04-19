# This file is executed on every boot (including wake-boot from deepsleep)
import uos as os
import uerrno as errno
iter = os.ilistdir()
IS_DIR = 0x4000
IS_REGULAR = 0x8000

# For successful boot display
from machine import Pin
import time
LED = Pin(2, Pin.OUT)
i = 0

while True:
    
    try:
        entry = next(iter)
        filename = entry[0]
        filetype = entry[1]
        if filename == 'PicoW_CaptivePControl.py':
            
            while i < 5:
                LED.value(0)
                time.sleep(0.5)
                LED.value(1)
                time.sleep(0.5)
                i = i+1
            LED.value(0) 
            exec(open(filename).read(),globals())
        else:
            continue
    except StopIteration:
        break