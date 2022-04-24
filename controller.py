from pyfirmata import Arduino, SERVO
import time

port = 'COM3'

pin = 10

board=Arduino(port)

board.digital[pin].mode=SERVO

def RotateServo(pin, angle):
    board.digital[pin].write(angle)

def BoxOpener(label):
    if label=="Mask":
        RotateServo(pin, 20)
        pass
    elif label=="No Mask":
        RotateServo(pin, 180)
        pass
