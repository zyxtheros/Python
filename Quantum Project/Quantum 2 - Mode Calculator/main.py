# Created By: Atilla Ozgur Cakmak, Caleb Capps
# Description:
# Calculating modes inside wells and barriers in order to find the
# transmission coefficient. The user enters beta value and E/V0 gets T

from math import *
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.offsetbox import AnchoredText
from matplotlib.widgets import Cursor, Slider
import cmath as cm

# Constants
m = 9.1e-31  # Mass of electron
h = 6.626e-34  # Planck's constant

# Variables
E = 1 * 1.6e-19  # Energy of the incoming electron
beta = 10  # Beta constant of the rectangular potential
E_over_V0 = float(input('Enter your E over V0 value'))  # E_over_V0 is entered by the user
A = 1  # Incoming wave function

# Definitions
V0 = E / E_over_V0
a = beta * h / (2 * pi) / sqrt(2 * m * abs(V0))  # Sorting out the thickness of the potential
k = cm.sqrt(2 * m * E) * 2 * pi / h  # Outside the potential wave function
k_p = cm.sqrt(2 * m * (E - V0)) * 2 * pi / h  # Inside the potential wave function

# Calculating B, C, F and G coefficients from TMM formulation
M11 = cm.cos(2 * k_p * a) + 1j / 2 * (k / k_p + k_p / k) * cm.sin(2 * k_p * a)
M12 = 1j / 2 * (k_p / k - k / k_p) * cm.sin(2 * k_p * a)
M21 = M12.conjugate()
M22 = M11.conjugate()

B = -M21 * A * cm.exp(-2 * 1j * k * a) / M22
C = (M11 * A * cm.exp(-1j * k * a) + M12 * B * cm.exp(1j * k * a)) * cm.exp(-1j * k * a)
F = (k_p + k) * cm.exp(1j * (k - k_p) * a) / (2 * k_p) * C
G = (k_p - k) * cm.exp(1j * (k + k_p) * a) / (2 * k_p) * C

# Plotting modes
x = np.linspace(-5 * a / 1000, 5 * a, int(4 * a * 1000))  # Independent variable array, sample space
Psi_L = A * cm.exp(1j * k * x) # + B * cm.exp(-1j * k * x)
Psi_I = F * cm.exp(1j * k_p * x) + G * cm.exp(-1j * k_p * x)
Psi_R = C * cm.exp(1j * k * x)
