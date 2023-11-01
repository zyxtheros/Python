# Precondition:     pushbutton connected to pin 11, drives high when pushed
#                   arduino Uno connected to COM port 6 and running the standard_firmata example sketch
# 
# Post-condition:   version number is displayed on screen, and True or False is printed to reflect if
#                   the button is pushed or not respectively

from pyfirmata import Arduino, util
from time import sleep

board = Arduino("COM6") # Set this to the corresponding COM port from the Arduino IDE

print("Running pyFirmata version " + str(board.get_firmata_version())) #Show firmata version

it = util.Iterator(board)
it.start()

button = board.get_pin('d:11:i')

sleep(1)
button.enable_reporting
while(1):
    print(button.read())
    sleep(0.25)