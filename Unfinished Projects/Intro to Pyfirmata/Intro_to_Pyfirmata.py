# package import assurance. If any of the following packages are missing, they will be added 
# as long as the pip package is already installed
try:
    import pip
except:
    print("Please install the package \"pip\" to continue")
try:
    from pyfirmata import Arduino, util
except:
    pip.main(['install','pyfirmata'])
    from pyfirmata import Arduino, util
try:
    import time
except:
    pip.main(['install','time'])
    import time

board = Arduino("COM6") # Set this to the corresponding COM port from the Arduino IDE

print("Running pyFirmata version " + str(board.get_firmata_version())) #Show firmata version

while(1):
    loopTimes = input("How many blinks would you like?\t")
    print("Blinking " + loopTimes + " Times")
    for x in range(int(loopTimes)):
        board.digital[13].write(1)  # write HIGH to pin 13 (internal LED)
        time.sleep(0.5)             # wait 0.5 seconds
        board.digital[13].write(0)  # write LOW to pin 13 (internal LED)
        time.sleep(0.5)             # wait 0.5 seconds

