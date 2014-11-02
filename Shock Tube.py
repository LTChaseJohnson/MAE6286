import numpy as np
import matplotlib.pyplot as plt

def f(u):
    return np.array([u[1],u[1]**2/u[0]+(gamma-1)*(u[2]-0.5*u[1]**2/u[0]),
    (u[2]+(gamma-1)*(u[2]-0.5*u[1]**2/u[0]))*u[1]/u[0]])

T = 0.1        #Final Time
dt = 0.0002
N = int(T/dt)+1
t = np.linspace(0.0, T, N)
nx = 81
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
u = np.empty((N,3))
u[0] = np.array([u0L,u1L,u2L])
u[-1] = np.array([u0R,u1R,u2R])