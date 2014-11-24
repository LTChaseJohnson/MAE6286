import numpy as np
import matplotlib.pyplot as plt
from scipy.linalg import solve

# Setting up Parameters
L = 1.
nt = 100
nx = 51
alpha = 1.22E-3

dx = L/(nx-1)
x = np.linspace(0,L,nx)

# Initial Conditions
Ti = np.zeros(nx)
Ti[0] = 100

def generateMatrix(N, sigma):
    # Builds Diagonal Values
    d = np.diag(np.ones(N-2)*(2+1./sigma))
    # Sets Boundary Condition
    d[-1,-1] = 1+1./sigma
    # Sets Upper Diagonal
    ud = np.diag(np.ones(N-3)*-1,1)
    #S Sets Lower Diagonal
    ld = np.diag(np.ones(N-3)*-1,-1)
    # Builds Full Matrix
    A = d+ud+ld
    
    return A

def RHS(T,sigma):
    b = np.zeros_like(T)
    b = T[1:-1]*1./sigma
    b[0] += T[0]
    
    return b

# Solving the Implicit Problem
def implicit_ftcs(T,A,nt,sigma):
    for t in range(nt):
        Tn = T.copy()
        b = RHS(Tn, sigma)
        T_i = solve(A,b)
        T[1:-1] = T_i
        T[-1] = T[-2]
        
    return T

sigma = 0.5
dt = sigma*dx**2/alpha
nt = 1000

A = generateMatrix(nx,sigma)

T = Ti.copy()
T = implicit_ftcs(T,A,nt,sigma)

plt.plot(x,T)

plt.show()