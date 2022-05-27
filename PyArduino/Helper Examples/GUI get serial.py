from tkinter import *
from time import sleep
import serial
arduinoData = serial.Serial('com3', 115200)
sleep(1) # allow time in the processor to setup the object



def getSerial():
    dataPacket = arduinoData.readline() # Get the COM data sent from the arduino
    dataPacket = str(dataPacket, 'utf-8') # convert the bytes back to string to remove secape chars
    dataPacket = dataPacket.strip('\r\n') # remove the extra reutrn from the decoding
    my_label1.config(text=dataPacket)

root = Tk()
root.geometry("500x400")

my_label1 = Label(root, text = float("0")+1)
my_label1.pack(pady = 20)

my_button1 = Button(root, text = "add 1:", command = getSerial)
my_button1.pack(pady = 20)
root.mainloop()

