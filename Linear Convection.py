import numpy as np
import matplotlib.pyplot as plt
from math import *

#Initial Conditions
nx = 50
nt = 10
c = 1.
x = np.linspace(0.0,2.,nx)
u = np.piecewise(x,[x<0.5,x>=0.5,x>=1.0],[1.0,2.0,1.0])
u0 = np.piecewise(x,[x<0.5,x>=0.5,x>=1.0],[1.0,2.0,1.0])
dt = 0.02
dx = 2./(nx-1)

for n in range(1,nt):
    un = u.copy()
    for i in range(1,nx):
        u[i] = un[i]-c*(dt/dx)*(un[i]-un[i-1])
        
plt.figure(1)
plt.title('Constant Velocity')
plt.plot(x,u0,label='Time Zero')
plt.plot(x,u,label='Time One')
plt.legend(loc='best')
plt.ylim(0.0,2.5)

#Variable Velocity
for n in range(1,nt):
    unv = u.copy()
    u[1:] = unv[1:]*(1-(dt/dx)*(unv[1:]-unv[0:-1]))

plt.figure(2)
plt.title('Variable Velocity')
plt.plot(x,u0,label='Time Zero')
plt.plot(x,u,label='Time One')
plt.legend(loc='best')
plt.ylim(0.,2.5)

plt.show()