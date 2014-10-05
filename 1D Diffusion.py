import numpy as np                  
import matplotlib.pyplot as plt    
from JSAnimation import IPython_display
from matplotlib import animation

nx = 41
dx = 2./(nx-1)
nt = 20
nu = 0.3
sigma = .2
dt = sigma*dx**2/nu

x = np.linspace(0.0,2.,nx)
u = np.piecewise(x,[x<0.5,x>=0.5,x>=1.0],[1.0,2.0,1.0])
u0 = np.piecewise(x,[x<0.5,x>=0.5,x>=1.0],[1.0,2.0,1.0])

for n in range(nt):
    un = u.copy()
    u[1:-1] = nu*dt/dx**2*(un[2:]-2*un[1:-1]+un[0:-2])+un[1:-1]
    
plt.figure(1)
plt.plot(x,u0,label='Time One')
plt.plot(x,u,label='Time Two')
plt.ylim(0,2.5)
plt.legend(loc='best')

fig = plt.figure(figsize=(8,5))
ax = plt.axes(xlim=(0,2), ylim=(1,2.5))
line = ax.plot([], [],)[0]

def diffusion(i):
    line.set_data(x,u)

    un = u.copy() 
    u[1:-1] = un[1:-1] + nu*dt/dx**2*(un[2:] -2*un[1:-1] +un[0:-2])

animation.FuncAnimation(fig,diffusion,frames=nt,interval=100)

plt.show()