import numpy as np
import matplotlib.pyplot as plt

def u_initial(nx,u_max,u_init):
    u = u_max*np.ones(nx)
    u[(nx-1)*2./4:] = u_init
    return u

<<<<<<< HEAD
nx = 81.
u_max = 1.0
u_init = 0.0
=======
nx = 81
u_max = 1.0
u_init = 0.0
nt = 70
dx = 4./(nx-1)
>>>>>>> origin/master

u0 = u_initial(nx,u_max,u_init)
x = np.linspace(0,4,nx)

plt.figure(1)
plt.plot(x,u0)
plt.ylim(-0.25,1.25)
plt.title('Initial Velocity')
plt.ylabel(r'$\frac{m}{s}$', size=16)
plt.xlabel(r'$m$', size=16)

<<<<<<< HEAD
plt.show()
=======
computeF = lambda u: (u/2)**2

def Maccormack(u,nt,dx):
    un = np.zeros((nt,len(u)))
    ustar = np.empty_like(u)
    un[:,:] = u.copy()
    ustar[:] = u.copy()
    
    for i in range(1,nt):
        F = computeF(u)
        
        ustar[:-1]=u[:-1]-dt/dx*(F[1:]-F[:-1])
        Fstar = computeF(ustar)
        
        un[i,1:]=0.5*(u[1:]+ustar[1:]-dt/dx*(Fstar[1:]-Fstar[:-1]))
        
        u = un[i].copy()
    
    return un

from matplotlib import animation
from JSAnimation.IPython_display import display_animation

def animate(data):
    x = np.linspace(0,4,nx)
    y = data
    line.set_data(x,y)
    return line,

u = u_initial(nx,u_max,u_init)
sigma = 1.
dt = sigma*dx

un = Maccormack(u,nt,dx)

fig = plt.figure();
ax = plt.axes(xlim=(0,4),ylim=(-.5,2))
line, = ax.plot([],[],lw=2);

anim = animation.FuncAnimation(fig, animate, frames = un, interval = 50)
display_animation(anim,default_mode='reflect')

def DampedMaccormack(epsilon,u,nt,dx):
    un = np.zeros((nt,len(u)))
    ustar = np.empty_like(u)
    un[:,:] = u.copy()
    ustar[:] = u.copy()
    
    for i in range(1,nt):
        F = computeF(u)
         
        
        ustar[1:-1]=u[1:-1]-dt/dx*(F[2:]-F[1:-1])+epsilon*(u[2:]-2*u[1:-1]+u[:-2])
        Fstar = computeF(ustar)
        
        un[i,1:]=0.5*(u[1:]+ustar[1:]-dt/dx*(Fstar[1:]-Fstar[:-1]))
        
        u = un[i].copy()
    
    return un

un = DampedMaccormack(0.35,u,nt,dx)

fig = plt.figure();
ax = plt.axes(xlim=(0,4),ylim=(-.5,2))
line, = ax.plot([],[],lw=2);

anim = animation.FuncAnimation(fig, animate, frames = un, interval = 50)
display_animation(anim,default_mode='reflect')

>>>>>>> origin/master
