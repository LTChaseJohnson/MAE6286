import numpy as np
import matplotlib.pyplot as plt

#Creates Initial Conditions
#Plucking the String
def u_initial(u_max,L):
    u = np.piecewise(x,[x<L/2,x>=L/2],[lambda x: 2*u_max/L*x,lambda x: 2*u_max*(-x/L+1)])
    return u

#Define Initial Parameters
u_max = 1.
L = 100.
nx = 100
x = np.linspace(0,L,nx)
dx = L/(nx-1)
nt = 500
c = 500.0
dt = 0.5*dx/c

g = lambda x: -2+2*np.cos(2*np.pi/L*x)
veli = g(x)
yi = u_initial(u_max,L)
lam = c*dt/dx
print lam**2

#Plot Initial Conditions
plt.plot(x,yi)
plt.plot(x,veli)
plt.xlim(0,L)
plt.figure(1)

def ctcs(nt,dt,ui,lam):
    yn = np.zeros((nt,len(yi)))
    yn[0,:] = ui
    y = yn.copy()
    y[0,1:-1] = yn[0,1:-1]
    y[1,1:-1] = y[0,1:-1]+dt*veli[1:-1] 
    for i in range(1,nt-1):
        y[i+1,1:-1] = 2*y[i,1:-1]*(1-lam**2)+lam**2*(y[i,2:]+y[i,:-2])-y[i-1,1:-1]
    return y

y = ctcs(nt,dt,yi,lam)

plt.figure(1)
plt.plot(x,y[1,:],label='Time 1')
plt.plot(x,y[2,:],label='Time 2')
plt.legend()

for i in range(nt):
    plt.figure(2)
    plt.plot(x,y[i,:])
    plt.xlim(0,L)
    
plt.show()

'''
from matplotlib import animation
from JSAnimation.IPython_display import display_animation

def animate(data):
    x = np.linspace(0,L,nx)
    y = data
    line.set_data(x,y)
    return line,

fig = plt.figure();
ax = plt.axes(xlim=(0,L),ylim=(-u_max,u_max))
line, = ax.plot([],[],lw=2);

anim = animation.FuncAnimation(fig, animate, frames = y, interval = 50)
display_animation(anim,default_mode='reflect')'''