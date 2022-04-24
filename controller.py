from pyfirmata import Arduino, SERVO
import time

port = 'COM3'

pin = 10

board=Arduino(port)

board.digital[pin].mode=SERVO

def RotateServo(pin, angle):
    board.digital[pin].write(angle)
    time.sleep(7)
    board.digital[pin].write(0)

def BoxOpener(label):
    if label=="Mask":
        pass
    elif label=="No Mask":
        RotateServo(pin, 180)
        pass
