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
        root.update_idletasks() # request a window update
        clock # run on a continuous cycle

def getSerial():
    dataPacket = arduinoData.readline() # Get the COM data sent from the arduino
    dataPacket = str(dataPacket, 'utf-8') # convert the bytes back to string to remove secape chars
    dataPacket = dataPacket.strip('\r\n') # remove the extra reutrn from the decoding
    my_label1.config(text=dataPacket)

root = Tk()
root.title("Userform HMI") # set the window title
root.geometry("500x400")

my_label1 = Label(root, text = "(X,Y,Z)")
my_label1.pack(pady = 20)

thread_clock = threading.Thread(target = clock)
thread_getSerial = threading.Thread(target = getSerial)


thread_clock.start()
root.mainloop()
