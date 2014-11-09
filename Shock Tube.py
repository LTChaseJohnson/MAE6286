import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation
from JSAnimation.IPython_display import display_animation

T = 0.01                      #Final Time
dt = 0.0002
nt = int(T/dt)
t = np.linspace(0.0, T, nt)   #Unnecessary (Only for plotting)
nx = 81
x = np.linspace(-10,10,nx)    #Unnecessary (Only for plotting)
dx = 0.25
gamma = 1.4
rhoL = 1
uL = 0
PL = 100E3
rhoR = 0.125
uR = 0
PR = 10E3

u0L = rhoL
u1L = uL
u2L = PL/(gamma-1)
u0R = rhoR
u1R = uR
u2R = PR/(gamma-1)

#Creating Space-U
uINIT = np.zeros((3,nx))
uINIT[0,nx/2.:]=u0R
uINIT[1,nx/2.:]=u1R
uINIT[2,nx/2.:]=u2R
uINIT[0,:nx/2.]=u0L
uINIT[1,:nx/2.]=u1L
uINIT[2,:nx/2.]=u2L

plt.figure(1)
plt.plot(x,uINIT[0],label='U1')
plt.legend(loc='best')
plt.figure(2)
plt.plot(x,uINIT[1],label='U2')
plt.legend(loc='best')
plt.figure(3)
plt.plot(x,uINIT[2],label='U3')
plt.legend(loc='best')

#Creating Space-Time-U Grid
usti = np.empty((3,nx,nt))
usti[:,:,0] = uINIT[:,:]

def f(u):
    f = np.array([u[1],u[1]**2/u[0]+(gamma-1)*(u[2]-.5*u[1]**2/u[0]),(u[2]+(gamma-1)*(u[2]-.5*u[1]**2/u[0]))*u[1]/u[0]])
    return f

def animate(data):
    x = np.linspace(-10,10,nx)
    y = data
    line.set_data(x,y)
    return line,

def Richtmyer(ust,nx,nt,dt,dx):
    un = ust[:,:,0]    
    ustarplus = np.zeros((3,nx))
    ustarminus = np.zeros((3,nx))
    
    for i in range(nt):
        ustarplus[:,0:-1] = 0.5*(un[:,1:]+un[:,0:-1])-0.5*dt/dx*(f(un[:,1:])-f(un[:,0:-1]))
        ustarminus[:,1:] = 0.5*(un[:,1:]+un[:,0:-1])-0.5*dt/dx*(f(un[:,1:])-f(un[:,0:-1]))
        un[:,1:-1] = un[:,1:-1]-dt/dx*(f(ustarplus[:,1:-1])-f(ustarminus[:,1:-1]))
              
        ust[:,:,i] = un[:,:]
        
    return ust

ust = Richtmyer(usti,nx,nt,dt,dx)

velocity = ust[1,:,:]/ust[0,:,:]
density = ust[0,:,:]
pressure = (gamma-1)*(ust[2,:,:]-0.5*(ust[1,:,:]**2/ust[0,:,:]))

pltvelocity = np.swapaxes(velocity,0,1)
pltdensity = np.swapaxes(density,0,1)
pltpressure = np.swapaxes(pressure,0,1)

U125=ust[0,50,-1]
U225=ust[1,50,-1]
U325=ust[2,50,-1]

print ('U1 at 2.5m: '),U125
print ('U2 at 2.5m: '),U225
print ('U3 at 2.5m: '),U325

u25 = U225/U125
P25 = (gamma-1)*(U325-.5*U225**2/U125)
rho25 = U125

print ('Velocity at 2.5m: '),u25
print ('Pressure at 2.5m: '),P25
print ('Density at 2.5m: '),rho25

fig = plt.figure();
ax = plt.axes(xlim=(-10,10),ylim=(0,600),xlabel=('Distance'),ylabel=('Velocity'));
line, = ax.plot([],[],color='k',lw=2);

anim =  animation.FuncAnimation(fig,animate,frames=pltvelocity[1:,:],interval=50)
display_animation(anim,default_mode='reflect')

fig = plt.figure();
ax = plt.axes(xlim=(-10,10),ylim=(0,1.1),xlabel=('Distance'),ylabel=('Density'));
line, = ax.plot([],[],color='k',lw=2);

anim =  animation.FuncAnimation(fig,animate,frames=pltdensity[1:,:],interval=50)
display_animation(anim,default_mode='reflect')

fig = plt.figure();
ax = plt.axes(xlim=(-10,10),ylim=(9900,101000),xlabel=('Distance'),ylabel=('Pressure'));
line, = ax.plot([],[],color='k',lw=2);

anim =  animation.FuncAnimation(fig,animate,frames=pltpressure[1:,:],interval=50)
display_animation(anim,default_mode='reflect')

def MUSCL(ust,nx,nt,dt,dx):
    un = ust[:,:,0]
    uni = ust[:,:,0]
    u_plus = np.zeros((3,nx))
    u_minus = np.zeros((3,nx))
    flux = np.zeros((3,nx))
    u_star = np.zeros((3,nx))
    
    for i in range(1,nt):
# * Step    
        u_plus[:,:-1] = un[:,1:]
        u_minus[:,:] = un[:,:]
    
        flux = 0.5*(f(u_minus)+f(u_plus)
                -dx/dt*(u_plus-u_minus))
        
        u_star[:,1:-1] = un[:,1:-1]+dt/dx*(flux[:,:-2]-
                                           flux[:,1:-1])
        u_star[:,0] = un[:,0]
        u_star[:,-1]  = un[:,-1]
# n+1 Step using * values
        u_plus[:,:-1] = u_star[:,1:]
        u_minus[:,:] = u_star[:,:]
    
        flux = 0.5*(f(u_minus)+f(u_plus)
                -dx/dt*(u_plus-u_minus))
    
        un[:,1:-1] = 0.5*(un[:,1:-1]+u_star[:,1:-1]+
                         dt/dx*(flux[:,:-2]-flux[:,1:-1]))
        
        ust[:,:,i] = un[:,:]
        ust[:,:,0] = uni[:,:]
    
    return ust  

ust = MUSCL(usti,nx,nt,dt,dx)

velocity = ust[1,:,:]/ust[0,:,:]
density = ust[0,:,:]
pressure = (gamma-1)*(ust[2,:,:]-0.5*(ust[1,:,:]**2/ust[0,:,:]))

pltvelocity = np.swapaxes(velocity,0,1)
pltdensity = np.swapaxes(density,0,1)
pltpressure = np.swapaxes(pressure,0,1)

fig = plt.figure();
ax = plt.axes(xlim=(-10,10),ylim=(0,600),xlabel=('Distance'),ylabel=('Velocity'));
line, = ax.plot([],[],color='k',lw=2);

anim =  animation.FuncAnimation(fig,animate,frames=pltvelocity[1:,:],interval=50)
display_animation(anim,default_mode='reflect')

fig = plt.figure();
ax = plt.axes(xlim=(-10,10),ylim=(0,1.1),xlabel=('Distance'),ylabel=('Density'));
line, = ax.plot([],[],color='k',lw=2);

anim =  animation.FuncAnimation(fig,animate,frames=pltdensity[1:,:],interval=50)
display_animation(anim,default_mode='reflect')

fig = plt.figure();
ax = plt.axes(xlim=(-10,10),ylim=(9900,101000),xlabel=('Distance'),ylabel=('Pressure'));
line, = ax.plot([],[],color='k',lw=2);

anim =  animation.FuncAnimation(fig,animate,frames=pltpressure[1:,:],interval=50)
display_animation(anim,default_mode='reflect')