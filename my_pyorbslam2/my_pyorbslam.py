import cv2
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def grab_frame(cap):
    ret,frame = cap.read()

    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    return frame

#Initiate the two cameras
cap1 = cv2.VideoCapture(0) # left stereo image
#cap2 = cv2.VideoCapture(0) # right stereo image

#create two subplots
ax1 = plt.subplot(1,2,1, label="Left")
ax2 = plt.subplot(1,2,2)

#create two image plots
im1 = ax1.imshow(grab_frame(cap1), cmap='gray')
im2 = ax2.imshow(grab_frame(cap1), cmap='gray')

#set the options for axes and titles
ax1.axis('off')
ax2.axis('off')
ax1.set_title("Left")
ax2.set_title("Right")

def update(i):
    im1.set_data(grab_frame(cap1))
    im2.set_data(grab_frame(cap1))
    
ani = FuncAnimation(plt.gcf(), update, interval=200)
plt.show()