from vpython import * # get the entire library
from time import *
from pymathjax import *

centerpoint = sphere(radius = 0.5, color = color.white)
x_axis = cylinder(axis=vector (1, 0, 0), color=color.red, length=1.5, width=0.25, height=0.25)
y_axis = cylinder(axis=vector(0, 1, 0), color=color.green, length=1.5, width=0.25, height=0.25)
z_axis = cylinder(axis=vector(0, 0, 1), color=color.blue, length=1.5, width=0.25, height=0.25)
origin = compound([x_axis, y_axis, z_axis, centerpoint])

wall1 = box(pos=vector(0, -5, 0), color = color.white, length=10, width=10, height=0.1) # length = X,width =Z, height =Y
wall2 = box(pos=vector(-5, 0, 0), color = color.white, length=0.1, width=10, height=10)
wall3 = box(pos=vector(0, 0, -5), color = color.white, length=10, width=0.1, height=10)
wallcorner = sphere(pos =vector(-5, -5, -5), color = color.red, radius = 0.2) # Coordinate location
stage = compound([wall1, wall2, wall3, wallcorner], origin = vector(-5, -5, -5)) # group the walls together along with the corner sphere

fps = 30
increment = 1
speed = vector (increment/fps, increment/fps, increment/fps) # movement speed of the stage
stageStartPos = vector (-5, -5, -5)

scene.camera.pos.x = scene.camera.pos.x +1
sleep(3)
scene.camera.pos.x = scene.camera.pos.x -1
startaxis = scene.camera.axis
startpos = scene.camera.pos
startDist = scene.forward
startRange = scene.range

# GUI elements
def btn_camerareset(b):
	print("The perspective has been reset") # print out to console
	scene.camera.axis = startaxis
	scene.camera.pos = startpos
	scene.forward = startDist


# def btn2():
# 	# print out to the user:
# 	scene.caption = ""
# 	scene.append_to_caption("-----------------------------------\n")
# 	scene.append_to_caption("axis is: ", scene.camera.axis, "\n")
# 	scene.append_to_caption("position is: ", scene.camera.pos, "\n")
# 	scene.append_to_caption("distance is: ", scene.forward, "\n")
# 	scene.append_to_caption("-----------------------------------\n")


button(bind=btn_camerareset, text='Reset View') # bind is the function to be called when clicked
# button(bind=btn2, text='Print Orientation')
scene.append_to_caption("\n\n")
wtext(text="axis is: ")
wtext(bind=scene.camera.axis)
wtext(text="\nposition is: ")
wtext(text=scene.camera.pos)
wtext(text="\ndistance is: ")
wtext(text=scene.forward)
wtext(text="\n")

scene.waitfor('click') 	# wait for mouse button click before storing the start position
						# required because vpython will not update the values until canvas
						# is activated by the user
startaxis = scene.camera.axis
startpos = scene.camera.pos
# btn2()
# box()
while True:

	# stage.pos = stage.pos + speed
	# sleep(1/fps)
	# if stage.pos == vector(0, 0 ,0):
	# 	speed = speed*-1
	# elif stage.pos == stageStartPos: 
	# 	speed = speed * -1

	# sleep(2)
	wtext(text="scene.camera.axis")
	pass


# def R(r):
# 	print(r.checked)  # alternates
# radio(bind=R, text='Run')  # text to right of button
# scene.append_to_caption('\n\n')
#
# def C(r):
# 	print(r.checked)  # alternates
# checkbox(bind=C, text='Run')  # text to right of checkbox
# scene.append_to_caption('\n\n')
#
# def S(s):
# 	print(s.value)
# slider(bind=S)
# scene.append_to_caption('\n\n')
#
# def M(m):
# 	print(m.selected, m.index)
# menu(choices=['cat', 'dog', 'horse'], bind=M)
# scene.append_to_caption('\n\n')
#
# def T(s):
# 	print(s.text, s.number)
# winput(bind=T)
#
# s = input('What is your name?')
#
# scene.title = "Hello"

# # extrusion examples
# tri = [ [2,0], [0,4], [-2,0], [2,0] ]
# circ = shapes.circle(radius=3)
# rect = shapes.rectangle(width=0.2, height=0.4)
# tripath = [ vec(1,0,0), vec(0,0,-2),
#             vec(-1,0,0), vec(1,0,0) ]
# circpath = paths.circle(radius=3)
# rectpath = paths.rectangle(width=4, height=2)
# arcpath = paths.arc(angle1=pi/4, angle2=pi)
# extrusion(path=circpath, shape=rect, color=color.red) # extrusion with predefined path
#
# extrusion(path=paths.circle(pos=vec(1,2,0)),
#          shape=shapes.rectangle(width=0.4, height=0.2),
#          up=vec(1,0,0), radius=2, color=color.cyan) # extrusion with path defined in call
