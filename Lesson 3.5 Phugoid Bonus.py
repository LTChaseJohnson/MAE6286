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

def eulerstep(u,f,dt):
    return u + dt * f(u)
    
def get_diffgrid(u_current,u_fine,dt):
    N_current = len(u_current[:,0])
    N_fine = len(u_fine[:,0])
    grid_size_ratio = np.ceil(N_fine/float(N_current))
    diffgrid = dt*np.sum(np.abs(u_current[:,2]-u_fine[::grid_size_ratio,2]))
    return diffgrid
    
def modeulerstep(u,f,dt):
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
    u_modeuler[n+1] = modeulerstep(u_modeuler[n],f,dt)

x_euler = u_euler[:,2]
y_euler = u_euler[:,3]

x_modeuler = u_modeuler[:,2]
y_modeuler = u_modeuler[:,3]

crash_index = np.where(y_euler<=0)[0][0]

#Let's see the plots!
plt.figure(1)
plt.grid(True)
plt.xlabel('x $m$')
plt.ylabel('Height $m$')
plt.plot(x_euler,y_euler,'k-',label='Euler')
plt.plot(x_modeuler,y_modeuler,'r--',label='Modified Euler')
plt.xlim(x0,x_euler[crash_index]+1)
plt.legend()
plt.ylim(0,2.5)

#Calculating multiple solutions with different dt
dt_values = np.array([0.1,0.05,0.01,0.005,0.001])
eu_values = np.empty_like(dt_values, dtype=np.ndarray)
mod_eu_values = np.empty_like(dt_values, dtype=np.ndarray)

for i, dt in enumerate(dt_values):
    N = int(T/dt)+1
    t = np.linspace(0.0,T,N)
    e = np.empty((N,4))
    e[0] = [v0,theta0,x0,y0]
    mod_e = np.empty((N,4))
    mod_e[0] = [v0,theta0,x0,y0]

for n in range(N-1):
    e[n+1] = eulerstep(e[n],f,dt)
    mod_e[n+1] = modeulerstep(mod_e[n],f,dt)


#Computing Difference Grid for Error Analysis
diffgrid_e = np.empty_like(dt_values)
diffgrid_mod_e = np.empty_like(dt_values)
for i, dt in enumerate(dt_values):
    diffgrid_e[i] = get_diffgrid(eu_values[i],eu_values[-1],dt)
    diffgrid_mod_e[i] = get_diffgrid(mod_eu_values[i],mod_eu_values[-1],dt)

plt.figure(2)
plt.grid(True)
plt.xlabel('$\Delta t$')
plt.ylabel('$L_1$')
plt.loglog(dt_values[:,-1],diffgrid_e[:,-1], color='k', ls='--',label='Euler')
plt.loglog(dt_values[:,-1],diffgrid_mod_e[:,-1], color='r', ls='--',label='Modified Euler')
plt.legend()

plt.show()