from servo import Servo
import time

def Open():
    motor=Servo(pin=22) 
    motor.move(180) # move servo to 180deg

def Close():
    motor=Servo(pin=22)
    motor.move(0) # move servo to 0deg