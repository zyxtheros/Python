# Quantum Transmission Coefficient
# Created By: Atilla Ozgur Cakmak, Caleb Capps
# Date: 3/28/21
# Description:
# this code will calculate the quantum transmission
# coefficient given a beta value for the quantum barrier

from math import *
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.offsetbox import AnchoredText
from matplotlib.widgets import Cursor, Slider
import cmath


def complex_sqr(n):
	return n*n


def onclick(event): # Define how to create the labels during plotting
	global coord
	global annotationCount
	global text
	global label
	coord.append((event.xdata, event.ydata))
	x[annotationCount] = event.xdata
	y[annotationCount] = event.ydata        # printing the values of the selected point
	print([x[annotationCount], y[annotationCount]])
	# print("annotationCount  = ", annotationCount)
	label[annotationCount].xy = (x[annotationCount], y[annotationCount])
	# Try to get set the XY coordinates, of out of bounds, None is returned
	try:
		text[annotationCount] = "({:.2g}, {:.2g})".format(x[annotationCount], y[annotationCount])
		label[annotationCount].set_text(text[annotationCount])
		label[annotationCount].set_visible(True)
		fig.canvas.draw()  # redraw the figure
		annotationCount = annotationCount + 1
	except:
		print("Label return failure")
		return


# Constants
m = 9.1e-31 # electron mass
h = 6.626e-34 # Planck's constant

# Plot setting:
x_start  = -5 # start position
x_stop   =  5 # end position
step_res = 0.0001 # resolution

# Variables
E = 1*1.6e-19 # energy of the incoming electron
E_over_V0 = np.linspace(x_start, x_stop, int((x_stop-x_start) * (1 / step_res)))
													# it is critical to define E/Vo first to avoid singularities

beta = input('Enter beta value (must be bigger than 0): ') # beta constant of the rectangular potential

# Create empty arrays for each variable
V0 = [0.0] * len(E_over_V0) # energy level of the rectangular potential
a = [0.0] * len(E_over_V0)
k_p = [0.0] * len(E_over_V0)
T = [0.0] * len(E_over_V0)
k = sqrt(2 * m * E) * 2 * pi / h  # free space wave vector

for i in range(len(E_over_V0)): # Populate the arrays
	V0[i] = E / E_over_V0[i]
	a[i] = float(beta) * h / (2 * pi) / sqrt(2 * m * abs(V0[i]))  # sorting out the thickness of the potential
	k_p[i] = cmath.sqrt(2 * m * (E - V0[i])) * 2 * pi / h  # k' wave vector inside the rectangular potential
	# calculating the transmission coefficient (T)
	T[i] = abs(1 / (1 + 1 / 4 * complex_sqr(k / k_p[i] - k_p[i] / k) * complex_sqr(cmath.sin(2 * k_p[i] * a[i]))))
	# print("E_overV0 =", E_over_V0[i], "\ta =", a[i], "\tT =", T[i])

fig = plt.figure()
ax = fig.subplots()
ax.plot(E_over_V0, T, linewidth=3)
ax.grid() # grid on
plt.title('Electron Interacting with the Potential', pad=10, y=-0.3)
at = AnchoredText(r'$\beta$ = ' + str(beta), prop=dict(size=15), frameon=True, loc='lower left')
at.patch.set_boxstyle("round,pad=0.,rounding_size=0.2")
ax.add_artist(at)
plt.xlabel(r'$E/V_0$ '+'(Electron Energy over Potential Energy)')
plt.ylabel('Transmission')

# AFTER PLOT CURSOR LABELS #
# Defining the cursor
cursor = Cursor(ax, horizOn=True, vertOn=True, useblit=True, color='r', linewidth=1)
coord = []

# create a variable to store up to 100 labels
annotationCount = 0
x = [0] * 100
y = [0] * 100
text = [0] * 100
label = [None] * 100
for i in range(len(label)):
	# Label properties
	label[i] = ax.annotate("", xy=(0, 0), xytext=(-40, 40),
						   textcoords="offset points", bbox=dict(boxstyle='round', fc='white', ec='k', lw=1),
						   arrowprops=dict(arrowstyle='-|>', facecolor='black'))
	label[i].set_visible(False)
fig.canvas.mpl_connect('button_press_event', onclick)

# SLIDER FOR BETA #

# for i in range(len(E_over_V0)):
# 	print("E_V0 ", E_over_V0[i], "T ", T[i])
plt.show()