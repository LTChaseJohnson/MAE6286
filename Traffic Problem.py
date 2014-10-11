import numpy as np
import matplotlib.pyplot as plt
from math import *

Vmax = 80. #km/hr
L = 11. #km
rhomax = 250. #cars/km
nx = 51
dt = 0.001 #hours
tf = input('Enter time (m): ')
tf1 = tf/60.
nt = int(tf1/dt) #How many dts are require to get to the time I'm interested in
dx = L/(nx-1)
print nt

x = np.linspace(0,L,nx)
rho0 = np.ones(nx)*10
rho0[10:20] = 50
rho = np.ones(nx)*10
rho[10:20] = 50

for n in range(1,nt):
    rhon = rho.copy()
    rho[1:]=-dt/dx*Vmax*(rhon[1:]*(1-rhon[1:]/rhomax)-rhon[0:-1]*(1-rhon[0:-1]/rhomax))+rhon[1:]
    rho[0]=10.
    
V = Vmax*(1-(rho/rhomax))

V0 = Vmax*(1-(rho0/rhomax))
    
plt.figure(1)
plt.title('Time Lapse Traffic Density')
plt.plot(x,rho,label='Time Step')
plt.plot(x,rho0,label='Time Zero')
plt.ylim(0,60)

plt.figure(2)
plt.show()