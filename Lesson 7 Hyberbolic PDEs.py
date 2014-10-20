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

def F(V_max, rho_max, rho):
    return V_max*rho*(1-rho/rho_max)

def animate(data):
    x = np.linspace(0,4,nx)
    y = data
    line.set_data(x,y)
    return line,

def LaxFred(rho, nt, dt, nx, rho_max, V_max):
    rhon = np.zeros((nt,len(rho)))
    rhon[:,:] = rho.copy()
    
    for t in range(1,nt):
        Flux = F(V_max, rho_max, rho)
        rhon[t,1:-1] = 0.5*(rho[2:]+rho[:-2])-dt/(2*dx)*(Flux[2:]-Flux[:-2])
        rhon[t,0] = rho[0]
        rhon[t,-1] = rho[-1]
        rho = rhon[t].copy()
    
    return rhon

sigma = 1.
dt = sigma*dx

rho = rho_red_light(nx, rho_max, rho_in)
rhon = LaxFred(rho, nt, dt, nx, rho_max, V_max)

fig = plt.figure()
ax = plt.axes(xlim=(0,4),ylim=(-.5,11),xlabel=('Distance'),ylabel=('Traffic Density'))
line, = ax.plot([],[],color='r',lw=2)

anim = animation.FuncAnimation(fig, animate, frames=rhon, interval=50)
display_animation(anim, default_mode='once')

def Maccormack(rho, nt, dt, dx, V_max, rho_max):
    rhon = np.zeros((nt,len(rho)))
    rho_star = np.empty_like(rho)
    rhon[:,:] = rho.copy()
    rho_star[:,:] = rho.copy()
    
    for t in range(1,nt):
        Flux = F(V_max, rho_max, rho)
        rho_star[:-1] = rho[:-1]-dt/dx*(Flux[1:]-Flux[:-1])
        Flux_star = F(V_max, rho_max, rho_star)
        rhon[t,1:] = 0.5*(rho[1:]+rho_star[1:]-dt/dx*(Flux_star[1:]-Flux_star[:-1]))
        
        rho = rhon[t].copy()
        
        return rhon

rho = rho_red_light(nx, rho_max, rho_in)
sigma = 1.0
dt = sigma*dx

rhon = Maccormack(rho, nt, dt, dx, V_max, rho_max)

fig = plt.figure()
ax = plt.axes(xlim=(0,4),ylim=(-.5,11),xlabel=('Distance'),ylabel=('Traffic Density'))
line, = ax.plot([],[],color='r',lw=2)

anim = animation.FuncAnimation(fig, animate, frames=rhon, interval=50)
display_animation(anim, default_mode='reflect')
        

plt.show()