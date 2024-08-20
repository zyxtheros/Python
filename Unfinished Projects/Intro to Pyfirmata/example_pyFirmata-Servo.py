# Precondition:     pushbutton connected to pin 11, drives high when pushed
#                   arduino Uno connected to COM port 6 and running the standard_firmata example sketch
# 
# Post-condition:   version number is displayed on screen, and True or False is printed to reflect if
#                   the button is pushed or not respectively

from pyfirmata import Arduino, SERVO, util
from time import sleep

board = Arduino("COM6") # Set this to the corresponding COM port from the Arduino IDE

print("Running pyFirmata version " + str(board.get_firmata_version())) #Show firmata version

board.digital[11].mode = SERVO

def rotateServo(pin, angle):
    board.digital[pin].write(angle)
    sleep(0.015) # short delay, not sure why this is necessary


while True:
    x=input("angle:\t")
    rotateServo(11, float(x))