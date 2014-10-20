import numpy as np
import matplotlib.pyplot as plt
from math import *
from matplotlib import animation
from JSAnimation.IPython_display import display_animation

#Defining our shock density and linear distribution
def rho_green_light(nx, rho_max, rho_light):
    rho = np.arange(nx)*2./nx*rho_light
    rho[(nx-1)/2:]=0
    return rho

#Defining initial conditions
nx = 81
nt = 30
dx = 4./nx

x = np.linspace(0,4,nx)

rho_max = 10.
V_max = 1.
rho_light = 10.

rho = rho_green_light(nx, rho_max, rho_light)

plt.plot(x,rho)
plt.ylabel('Traffic Density')
plt.xlabel('Distance')

#Traffic Flux function
def Flux(V_max, rho_max, rho):
    return V_max*rho*(1-rho/rho_max)

#Forward Time/Backward Space
def FTBS(rho, nt, dt, dx, rho_max, V_max):
    rhon = np.zeros((nt,len(rho)))
    rhon[0,:]=rho.copy()
    for t in range(1,nt):
        F=Flux(V_max, rho_max, rho)
        rhon[t,1:] = rho[1:] - dt/dx*(F[1:]-F[:-1])
        rhon[t,0] = rho[0]
        rhon[t,-1] = rho[-1]
        rho = rhon[t].copy()
    return rhon

#Running Forward Time/Backward Space
sigma = 1.
dt = sigma*dx

rhon = FTBS(rho, nt, dt, dx, rho_max, V_max)

fig = plt.figure();
ax = plt.axes(xlim=(0,4),ylim=(-.5,11),xlabel=('Distance'),ylabel=('Traffic Density'));
line, = ax.plot([],[],color='r',lw=2);

def animate(data):
    x = np.linspace(0,4,nx)
    y = data
    line.set_data(x,y)
    return line,

anim = animation.FuncAnimation(fig, animate, frames=rhon,interval=50)
display_animation(anim, default_mode='once')


plt.show()