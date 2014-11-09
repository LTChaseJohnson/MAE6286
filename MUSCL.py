import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation
from JSAnimation.IPython_display import display_animation

def rho_red_light(nx, rho_max,rho_in):
    rho = rho_max*np.ones(nx)
    rho[:(nx-1)*3./4] = rho_in
    return rho

def F(V_max, rho_max, rho):
    return V_max*rho*(1-rho/rho_max)

def minmod(e,dx):
    sigma - np.zeros_like(e)
    de_minus[1:] = e[1:] - e[:-1]
    de_plus[:-1] = e[:-1] - e[1:]
    for i in range(1,len(e)-1):
        if (de_minus[i]*de_plus[i] < 0.0):
            sigma[i] = 0.0
        elif (np.abs(de_minus[i]) < np.abs(de_plus[i])):
            sigma[i] = de_minus[i]
        else:
            sigma[i] = de_plus[i]
    return sigma

def animate(data):
    x = np.linspace(0,4,nx)
    y = data
    line.set_data(x,y)
    return line,

def MUSCL(rho,nt,dt,dx,rho_max,V_max):
    rho_n = np.zeros((nt,len(rho)))
    rho_n[:,:] = rho.copy()
    
    for t in range(1,nt):
# * Step    
        rho_plus = np.zeros_like(rho)
        rho_minus = np.zeros_like(rho)
        flux = np.zeros_like(rho)
        rho_star = np.zeros_like(rho)
    
        rho_plus[:-1] = rho[1:]
        rho_minus[:] = rho[:]
    
        flux = 0.5*(F(V_max,rho_max,rho_minus)
                +F(V_max,rho_max,rho_plus)
                -dx/dt*(rho_plus-rho_minus))
        rho_star[1:-1] = rho[1:-1]+dt/dx*(flux[:-2]-flux[1:-1])
        rho_star[0] = rho[0]
        rho_star[-1]  = rho[-1]
# n+1 Step using * values
        rho_plus[:-1] = rho_star[1:]
        rho_minus[:] = rho_star[:]
    
        flux = 0.5*(F(V_max,rho_max,rho_minus)
                +F(V_max,rho_max,rho_plus)
                -dx/dt*(rho_plus-rho_minus))
    
        rho_n[t,1:-1] = 0.5*(rho[1:-1]+rho_star[1:-1]+
                         dt/dx*(flux[:-2]-flux[1:-1]))
        rho_n[t,0] = rho[0]
        rho_n[t,-1] = rho[-1]
        rho = rho_n[t].copy()
    
    return rho_n    

nx = 81
nt = 30
dx = 4./nx

rho_in = 5.
rho_max = 10.
V_max = 1.

x = np.linspace(0,4,nx)

rho = rho_red_light(nx,rho_max,rho_in)

sigma = 1.
dt = sigma*dx

rho_n = MUSCL(rho,nt,dt,dx,rho_max,V_max)

fig = plt.figure();
ax = plt.axes(xlim=(0,4),ylim=(4.5,11),xlabel=('Distance'),ylabel=('Traffic Density'));
line, = ax.plot([],[],color='k',lw=2);

anim =  animation.FuncAnimation(fig,animate,frames=rho_n,interval=50)
display_animation(anim,default_mode='reflect')