from tkinter import *
from time import sleep

def addone():
    tmp = float(my_label1["text"])+1
    my_label1.config(text=tmp)

root = Tk()
root.geometry("500x400")

my_label1 = Label(root, text = float("0")+1)
my_label1.pack(pady = 20)

my_button1 = Button(root, text = "add 1:", command = addone)
my_button1.pack(pady = 20)
root.mainloop()

