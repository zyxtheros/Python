import time
import serial
arduinoData = serial.Serial('com3', 115200)
time.sleep(1) # allow time in the processor to setup the object, 1-second


while True:
    while (arduinoData.inWaiting() == 0):
        pass
    dataPacket = arduinoData.readline() # Get the COM data sent from the arduino
    dataPacket = str(dataPacket, 'utf-8') # convert the bytes back to string to remove secape chars
    dataPacket = dataPacket.strip('\r\n') # remove the extra reutrn from the decoding
    splitPacket = dataPacket.split(", ") # Tokenize the string into individual numbers
    for item in range(0, len(splitPacket)): # convert the packet items to floats
        splitPacket[item] = float(splitPacket[item])
    print(splitPacket)