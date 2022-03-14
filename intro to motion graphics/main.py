# basic animation with python
import turtle
import time

### GLOBAL VARIABLES ###

win = turtle.Screen() # create an instance of a screen
win.title("ANIMATION DEMO") # window title
win.bgcolor("black") # set the background color

# Register shapes
win.register_shape("invader.gif")
win.register_shape("invader2.gif")

class Player(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.penup()
        self.shape("invader.gif")  # set the entity shape
        self.color("green")  # set the entity color
        self.frame = 0  # set the initial frame number
        self.frames = ["invader.gif", "invader2.gif"]

    def animate(self):
        self.frame += 1
        if self.frame >= len(self.frames):
            self.frame = 0  # reset the frame count
        self.shape(self.frames[self.frame])

        # Set timer for time between each frame
        win.ontimer(self.animate, 500)

player = Player() # create a new entity instance
player2 = Player()
player2.goto(-100, 0)

# RUN CONDITIONS

player2.animate()
player.animate()

while True:
    win.update() # pause before updating
    print("MAIN LOOP")



win.mainloop() # keep the window open