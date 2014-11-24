import numpy as np
import matplotlib.pyplot as plt

# Constants and Parameters
L = 1.
nt = 100
nx = 51
alpha = 1.22E-3
x = np.linspace(0,L,nx)

dx = (L)/(nx-1)

# Initial Condition on left hand side
Ti = np.zeros(nx)
Ti[0] = 100

def ftcs(T, nt, dt, dx, alpha):
    for n in range(nt):
        Tn = T.copy()
        T[1:-1] = Tn[1:-1] + alpha*dt/dx**2*(Tn[2:]-2*Tn[1:-1]+Tn[:-2])
    return T

# CFL Condition
sigma = .5
dt = sigma*dx**2/alpha

# Setting up Problem
T = ftcs(Ti,nt,dt,dx,alpha)

#Plotting Solution
plt.figure(1)
plt.plot(x,T)
plt.ylim(0,100)
plt.xlabel('Length of Rod')
plt.ylabel('Temperature')

plt.show()