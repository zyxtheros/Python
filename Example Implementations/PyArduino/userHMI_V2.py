from tkinter import *
from time import sleep
import serial
import threading
from classes.gui import * # Add custom GUI class

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

def test():
    print("Hello")

root = Tk()
root.title("Userform HMI") # set the window title
root.geometry("1000x600")

my_label1 = Label(root, text = "(X,Y,Z)")
my_label1.pack(pady = 20)

canvas = Canvas(root, height=600, width=1000)
canvas.pack()

button = RoundedButton(root, 150, 35, 15, 0, palette.primaryDark, 'white', command=test)
button.place(relx=0, rely=0)

thread_clock = threading.Thread(target = clock)
thread_getSerial = threading.Thread(target = getSerial)


thread_clock.start()
root.mainloop()
