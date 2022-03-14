# basic animation with python
import turtle
import time

# GLOBAL VARIABLES

win = turtle.Screen() # create an instance of a screen
win.title("ANIMATION DEMO") # window title
win.bgcolor("black") # set the background color

player = turtle.Turtle() # create a new entity
player.shape("square") # set the entity shape
player.color("green") # set the entity color



# RUN CONDITIONS
def player_animate():
    if player.shape() == "square":
        player.shape("circle")
    elif player.shape() == "circle":
        player.shape("square")

    # Set timer
    win.ontimer(player_animate, 500)

player_animate()

while True:
    win.update() # pause before updating
    print("MAIN LOOP")



win.mainloop() # keep the window open