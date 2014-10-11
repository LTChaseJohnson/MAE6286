import numpy as np
import matplotlib.pyplot as plt
from math import *

Vmax = 136. #km/hr
L = 11. #km
rhomax = 250. #cars/km
nx = 51
dt = 0.001 #hours
tf = input('Enter time (m): ')
tf1 = tf/60.
nt = int(tf1/dt) #How many dts are require to get to the time I'm interested in
dx = L/(nx-1)

x = np.linspace(0,L,nx)
rho0 = np.ones(nx)*20
rho0[10:20] = 50
rho = np.ones(nx)*20
rho[10:20] = 50

for n in range(1,nt):
    rhon = rho.copy()
    rho[1:]=-dt/dx*Vmax*(rhon[1:]*(1-rhon[1:]/rhomax)-rhon[0:-1]*(1-rhon[0:-1]/rhomax))+rhon[1:]
    rho[0]=20.
    
V = (0.2778)*Vmax*(1-(rho/rhomax))

V0 = (0.2778)*Vmax*(1-(rho0/rhomax))

V0min = min(V0)
V0avg = np.average(V0)

Vmin = min(V)
Vavg = np.average(V)

print('Minimum velocity at t=0m: '),'%0.2f' %V0min
print('Average velocity at t=0m: '),'%0.2f' %V0avg

print('Minimum velocity at t=%0.1fm: '%tf),'%0.2f' %Vmin
print('Average velocity at t=%0.1fm: '%tf),'%0.2f' %Vavg
    
plt.figure(1)
plt.title('Time Lapse Traffic Density')
plt.plot(x,rho,label='Time Step')
plt.plot(x,rho0,label='Time Zero')
plt.ylabel(r'$\rho (\frac{cars}{km})$',size=16)
plt.xlabel(r'$x(km)$',size=16)
plt.ylim(0,60)

plt.figure(2)
plt.title('Time Lapse Traffic Velocity')
plt.plot(x,V0,label='Time Zero')
plt.plot(x,V,label='Time Step')
plt.ylabel(r'$V (\frac{m}{s})$',size=16)
plt.xlabel(r'$x(km)$',size=16)
plt.ylim(min(V0)-5,max(V0)+5)
plt.show()