import numpy as np
import matplotlib.pyplot as plt
from math import *
'''from matplotlib import animation
from JSAnimation.IPython_display import display_animation'''

def rho_red_light(nx, rho_max,rho_in):
    rho = rho_max*np.ones(nx)
    rho[:(nx-1)*3./4] = rho_in
    return rho

nx = 81
nt = 30
dx = 4./nx

rho_in = 5.
rho_max = 10.

V_max = 1.

x = np.linspace(0,4,nx)

rho = rho_red_light(nx, rho_max, rho_in)

plt.plot(x,rho)
plt.ylabel('Traffic Density')
plt.xlabel('Distance')
plt.ylim(-.5,11)
plt.show()