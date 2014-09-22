import numpy as np
import matplotlib.pyplot as plt
from math import *

#Model Parameters:
g = 9.8             #Gravitational acceleration (m/s**2)
v_t = 4.9           #Trim velocity (m/s)
Cd = 1/5.0          #Drag coefficient
Cl = 1.0            #Lift coefficient

#Initial Conditions:
v0 = 6.5            #Initial velocity (m/s)
theta0 = -0.1       #Initial angle (radians)
x0 = 0.0            #Initial x position (m)
y0 = 2.0            #Initial y position (m)

def f(u):
    v = u[0]
    theta = u[1]
    x = u[2]
    y = u[3]
    return np.array([-g*np.sin(theta)-(Cd/Cl)*(g/v_t**2)*v**2,
                      -(g/v)*np.cos(theta)+(g/v_t**2)*v,
                      v*np.cos(theta),
                      v*np.sin(theta)])

def eulerstep(f,u,dt):
    return u + dt * f(u)
    
def get_diffgrid(u_current,u_fine,dt):
    N_current = len(u_current[:,0])
    N_fine = len(u_fine[:,0])
    grid_size_ratio = np.ceil(N_fine/float(N_current))
    diffgrid = dt*np.sum(np.abs(u_current[:,2]-u_fine[::grid_size_ratio,2]))
    return diffgrid
    
def modeulerstep(f,u,dt):
    u_half = u + 0.5*dt*f(u)
    return u + dt*f(u_half)

#Defining time step parameters
T = 15.0
dt = 0.01
N = int(T/dt)+1

#Creating empty solution vectors
u_euler = np.empty((N,4))
u_modeuler = np.empty((N,4))

#Storing initial conditions
u_euler[0] = np.array([v0,theta0,x0,y0])
u_modeuler[0] = np.array([v0,theta0,x0,y0])

#Running the Loop!
for n in range(N-1):
    u_euler[n+1] = eulerstep(u_euler[n],f,dt)
    if u_euler[n+1]<0.0:
        break
    u_modeuler[n+1] = modeulerstep(u_modeuler[n],f,dt)
    if u_modeuler[n+1]<0.0:
        break

x_euler = u_euler[:,2]
y_euler = u_euler[:,3]

x_modeuler = u_modeuler[:,2]
y_modeuler = u_modeuler[:,3]

