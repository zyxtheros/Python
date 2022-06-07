from tkinter import *
from time import sleep
import serial
import threading

arduinoData = serial.Serial('com3', 115200)
sleep(1) # allow time in the processor to setup the object, 1-second

def five_seconds():
    my_label.config(text = "Timer started!")
    sleep(5)
    my_label.config(text = "Your time is up")


def addone():
    tmp = float(my_label2["text"])+1
    my_label2.config(text=tmp)

root = Tk()
root.geometry("1000x600")

my_label = Label(root, text = "Hello there")
my_label.pack(pady = 20)

my_button1 = Button(root, text = "5 seconds", command = threading.Thread(target = five_seconds).start())
my_button1.pack(pady = 20)

global counter
counter = 0

my_label2 = Label(root, text = float("0")+1)
my_label2.pack(pady = 20)

my_button2 = Button(root, text = "add 1:", command = addone)
my_button2.pack(pady = 20)
root.mainloop()

