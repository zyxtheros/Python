from tkinter import *
from time import sleep
import serial
import threading
arduinoData = serial.Serial('com3', 115200)
sleep(1) # allow time in the processor to setup the object

def clock():
    while True:
        sleep(1)
        getSerial()

        @SerialParse_csv
        getSerial()

        root.update_idletasks() # request a window update
        clock # run on a continuous cycle
"""
    Parse input data separated by commas into usable float values
    decorator for the getSerial function
"""
def SerialParse_csv(func):
    def inner():
        func()
        splitPacket = dataPacket.split(", ") # Tokenize the string into individual numbers
        for item in range(0, len(splitPacket)): # convert the packet items to floats
            splitPacket[item] = float(splitPacket[item])
        print(splitPacket+1)

    return splitPacket

    

@SerialParse_csv
def getSerial():
    dataPacket = arduinoData.readline() # Get the COM data sent from the arduino
    dataPacket = str(dataPacket, 'utf-8') # convert the bytes back to string to remove escape chars
    dataPacket = dataPacket.strip('\r\n') # remove the extra return from the decoding
    my_label1.config(text=dataPacket)

root = Tk()
root.title("Userform HMI") # set the window title
root.geometry("500x400")

my_label1 = Label(root, text = "(X,Y,Z)")
my_label1.pack(pady = 20)
my_label2 = Label(root, text = "(X+1,Y+1,Z+1)")
my_label2.pack(pady = 20)

thread_clock = threading.Thread(target = clock)
thread_getSerial = threading.Thread(target = getSerial)


thread_clock.start()
root.mainloop()
