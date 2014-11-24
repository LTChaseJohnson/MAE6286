import numpy as np
import matplotlib.pyplot as plt

# Constants and Parameters
L = 1.
nt = 100
nx = 51
alpha = 1.22E-3

dx = (L)/(nx-1)

# Initial Condition on left hand side
Ti = np.zeros(nx)
Ti[0] = 100

