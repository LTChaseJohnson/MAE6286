import numpy as np
import matplotlib.pyplot as plt

def f(u):
    return np.array([u[1],u[1]**2/u[0]+(gamma-1)*(u[2]-0.5*u[1]**2/u[0]),
    (u[2]+(gamma-1)*(u[2]-0.5*u[1]**2/u[0]))*u[1]/u[0]])

T = 0.1        #Final Time
dt = 0.0002
nt = int(T/dt)+1
t = np.linspace(0.0, T, N)  #Unnecessary
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
u = np.zeros((3,nx))
u[0,0]=u0L
u[1,0]=u1L
u[2,0]=u2L
u[0,-1]=u0R
u[1,-1]=u1R
u[2,-1]=u2R
#Creating Space-Time-U
ust = np.empty((3,nx,nt))
ust[:,:,0] = u[:,:]


def f(u):
    f = np.array([u[1],u[1]**2/u[0]+(gamma-1)*(u[2]-.5*u[1]**2/u[0]),(u[2]+(gamma-1)*(u[2]-.5*u[1]**2/u[0]))*u[1]/u[0]])
    return f

def Richtmyer(u,nx,nt,dt,dx):
    un = np.empty_like(u)
    ustarplus = u.copy()
    ustarminus = u.copy()
    
    for i in range(nt):
        ustarplus[:,:,-1] = 0.5*(u[i,0:]+u[i,:-1])-0.5*dt/dx*(f(u[i,0:])-f(u[:,:-1]))
        ustarminus[i] = 0.5*(u[i,0:]+u[i,:-1])-0.5*dt/dx*(f(u[i,0:])-f(u[i,:-1]))
        Fstarplus[i] = F(ustarplus[i])
        Fstarminus[i] = F(ustarminus[i])
        un[i,