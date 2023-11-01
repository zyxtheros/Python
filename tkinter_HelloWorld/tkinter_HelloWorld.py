# importing only those functions 
# which are needed 
import tkinter as tk
from PIL import Image, ImageTk
import sys

# Create a function to increment the value and update the button text
def increment_value():
    current_value = int(btn["text"])
    new_value = current_value + 1
    btn.config(text=str(new_value))


def int_rescale(scalar: float, val: tuple, show_output = False):
    tup = ([int(scalar*x) for x in val])
    if show_output:
        print(f"Size went from {val} to {tup}")
    return tup

# creating tkinter window 
root = tk.Tk() 
  
#Adding widgets to the root window 
label = tk.Label(root, text="TEST").pack() # Create a label to display the value

if getattr(sys, 'frozen', False):
    photo = Image.open(os.path.join(sys._MEIPASS, "stockart_container.png"))
else:
    photo = Image.open("stockart_container.png")

#photo = Image.open("stockart_container.png") # Creating a Image object
scale = 0.1 # percentage of the original size
photo = photo.resize(int_rescale(scale, photo.size)) # resize the image by a pixed percentage (keep aspect ratio)
photo = ImageTk.PhotoImage(photo) # convert back to a usable tkinter image
  
# here, image option is used to set image on button 
# compound option is used to align image on TOP side of button 
btn = tk.Button(root, text = "0", image = photo, command = increment_value, compound = tk.TOP)
btn.pack()
tk.mainloop() 
