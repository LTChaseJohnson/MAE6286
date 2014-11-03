import numpy as np
import matplotlib.pyplot as plt

def f(u):
    return np.array([u[1],u[1]**2/u[0]+(gamma-1)*(u[2]-0.5*u[1]**2/u[0]),
    (u[2]+(gamma-1)*(u[2]-0.5*u[1]**2/u[0]))*u[1]/u[0]])

T = 0.1        #Final Time
dt = 0.0002
nt = int(T/dt)+1
t = np.linspace(0.0, T, nt)  #Unnecessary
nx = 81
x = np.linspace(-10,10,nx)  #Unnecessary
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
uINIT[0,0]=u0L
uINIT[1,0]=u1L
uINIT[2,0]=u2L
uINIT[0,-1]=u0R
uINIT[1,-1]=u1R
uINIT[2,-1]=u2R
#Creating Space-Time-U
ust = np.empty((3,nx,nt))
ust[:,:,0] = uINIT[:,:]


def f(u):
    f = np.array([u[1],u[1]**2/u[0]+(gamma-1)*(u[2]-.5*u[1]**2/u[0]),(u[2]+(gamma-1)*(u[2]-.5*u[1]**2/u[0]))*u[1]/u[0]])
    return f

def Richtmyer(ust,nx,nt,dt,dx):
    un = ust[:,:,0]    #This needs to remain the same dimensions as ust
    ustarplus = un.copy()       #This is one less dimension and will roll through time adding values to ust
    ustarminus = un.copy()
    
    for i in range(1,nt):
        ustarplus[:,:-1] = 0.5*(un[:,0:-1]+un[:,:-1])-0.5*dt/dx*(f(un[:,0:-1])-f(un[:,:-1]))
        ustarminus[:,0:-1] = 0.5*(un[:,0:-1]+un[:,:-1])-0.5*dt/dx*(f(un[:,0:-1])-f(un[:,:-1]))
        un[:,1:-1] = un[:,1:-1]-dt/dx*(f(ustarplus[:,1:-1])-f(ustarminus[:,1:-1]))
        
        ust[:,:,i] = un[:,:]
        
    return ust

u = Richtmyer(ust,nx,nt,dt,dx)

U125=u[0,50,-1]
U225=u[1,50,-1]
U325=u[2,50,-1]

print ('U1 at 2.5m: '),U125
print ('U2 at 2.5m: '),U225
print ('U3 at 2.5m: '),U325

u25 = U225/U125
P25 = (gamma-1)*(U325-.5*U225**2/U125)
rho25 = U125

print ('Velocity at 2.5m: '),u25
print ('Pressure at 2.5m: '),P25
print ('Density at 2.5m: '),rho25