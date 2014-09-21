from math import *
import numpy as np
import matplotlib.pyplot as plt

# Constants
g = 9.8                #Gravitational acceleration
v_t = 4.9              #Trim velocity
C_D = 1/5.             #Drag Coefficient
C_L = 1.               #Lift Coefficient

# Initial Conditions
x0 = 0.                 #Horizontal start point
y0 = 1.5                #Initial altitude
theta_iter=np.linspace(-pi/4.,pi/4.,100)     #Steps of angle
theta0=0.
v_iter=np.linspace(0.01,10,100)           #Steps of velocity
v0=0.01



def f(u):               #Creates system of equations u'(t)=f(u)
    v = u[0]
    theta = u[1]
    x = u[2]
    y = u[3]
    return np.array([-g*np.sin(theta)-(C_D/C_L)*(g/v_t**2)*v**2,
                     -(g/v)*np.cos(theta)+(g/v_t**2)*v,
                     v*np.cos(theta),
                     v*np.sin(theta)])
                     
def euler_step(u,f,dt):
    return u + dt*f(u)

T = 100                  #Final time
dt = input('Enter time step: ')
N = int(T/dt) + 1        #Number of time steps
t = np.linspace(0.0,T,N)
sol_mat=np.array([0.0,0.0,0.0,0.0])

u = np.empty((N,4))                           #Empty matrix of N columns and 4 rows for system of equation

for v0 in v_iter:
    for theta0 in theta_iter:
        u[0] = np.array([v0,theta0,x0,y0])    #First column is initial conditions
        for n in range(N-1):                 #This will populate empty u vector!
            u[n+1] = euler_step(u[n],f,dt)
            if u[n+1,3]<=0:                  #This tells me when it hits the ground
                if u[n+1,2]>sol_mat[3]:
                    sol_mat[3]=u[n+1][3]
                    sol_mat[2]=u[n+1][2]
                    sol_mat[1]=u[n+1][1]
                    sol_mat[0]=u[n+1][0]
                break
print sol_mat
                
                
#Need to know when y=0.
#Find the corresponding x value
#Change theta and compare new x value
#Go through theta_iter and find max x and define theta