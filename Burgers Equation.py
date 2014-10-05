import numpy as np
import sympy
from math import *
import matplotlib.pyplot as plt
from sympy.utilities.lambdify import lambdify
from sympy import init_printing
init_printing()

# Defining Symbolic Equations
x, nu, t = sympy.symbols('x nu t')
phi = sympy.exp(-(x-4*t)**2/(4*nu*(t+1)))+sympy.exp(-(x-4*t-2*np.pi)**2/(4*nu*(t+1)))
phiprimex = phi.diff(x)
u = -(2*nu*phiprimex/phi)+4
functionu = lambdify((t,x,nu),u)
phi
phiprimex
u

nx = 101
nt = 100
dx = 2*np.pi/(nx-1)
nu = 0.07
dt = dx*nu

x = np.linspace(0,2*np.pi,nx)
un = np.empty(nx)
t=0

#Creating the compression loop
u = np.asarray([functionu(t,x0,nu) for x0 in x])

#Plotting Initial Conditions
plt.figure(1)
plt.plot(x,u)
plt.xlim(0,2*np.pi)
plt.ylim(0,10)

#Creating analytical loop solution
for n in range(nt):
    un = u.copy()
    u[1:-1] = un[1:-1]-un[1:-1]*dt/dx*(un[1:-1]-un[:-2])+nu*dt/dx**2*(un[2:]+un[:-2]-2*un[1:-1])
    u[0] = un[0]-un[0]*dt/dx*(un[0]-un[-1])+nu*dt/dx**2*(un[1]+un[-1]-2*un[0])
    u[-1] = un[-1]-un[-1]*dt/dx*(un[-1]-un[-2])+nu*dt/dx**2*(un[-2]+un[0]-2*un[-1])

u_analytical = np.asarray([functionu(nt*dt,xi,nu) for xi in x])

#Plotting Solutions
plt.figure(2)
plt.plot(x,u,label='Computational')
plt.plot(x,u_analytical,label='Analytical')
plt.xlim(0,2*np.pi)
plt.ylim(0,10)
plt.legend(loc='best')

#Running Timed Animation
from JSAnimation.IPython_display import display_animation
from matplotlib import animation

u = np.asarray([functionu(t,x0,nu) for x0 in x])

fig = plt.figure(figsize=(8,6))
ax = plt.axes(xlim=(0,2*np.pi), ylim=(0,10))
line = ax.plot([], [], 'r', ls='--',lw=3)[0]
line2 = ax.plot([] ,[], 'k', lw=2)[0]
ax.legend(['Computed','Analytical'])

plt.show()

def burgers(n):
     un = u.copy()
     u[1:-1] = un[1:-1]-un[1:-1]*dt/dx*(un[1:-1]-un[:-2])+nu*dt/dx**2*(un[2:]+un[:-2]-2*un[1:-1])
     u[0] = un[0]-un[0]*dt/dx*(un[0]-un[-1])+nu*dt/dx**2*(un[1]+un[-1]-2*un[0])
     u[-1] = un[-1]-un[-1]*dt/dx*(un[-1]-un[-2])+nu*dt/dx**2*(un[-2]+un[0]-2*un[-1])
     
     u_analytical = np.asarray([functionu(n*dt, xi, nu) for xi in x])
     line.set_data(x,u)
     line2.set_data(x,u_analytical)

animation.FuncAnimation(fig, burgers, frames=nt, interval=100)