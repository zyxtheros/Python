# Gyrometer Test Program

from math import *
import numpy as np

# Create gyrometer and accelerometer simulation parameters
rollTruek1 = 0.0
rollTruek = 0.0
rollVelTrue = 0.0

gyroDriftTrue = 1.0
gyroCalBiasTrue = 0.01
gyroSigmaNoise = 0.002
accellSigmaNoise = sqrt(0.03)

accelMeask1 = 0.0
accelMeask = 0.0
gyroMeask1 = 0.0
gyroMeask = 0.0

frequency = 250.0       # 250 Hz
deltaT = 1/frequency    # Time step
dataStore = np.zeros((5010, 7), dtype=float)    # Data storage array

# Create complementary filter parameters
angleRollK1 = 0.0
angleRollK = 0.0

gainK1 = 0.99   # Gyro gain
gainK2 = 0.01   # Gyro drift correction gain via accelerometer

# Create Kalman filter parameters
xk = np.zeros((1,2), dtype = float)
pk[] = {0.5, 0, 0, 0.01}
K = np.zeros((1,2), dtype = float)
phi[] = {}

