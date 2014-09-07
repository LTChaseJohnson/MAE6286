import numpy as np                    #Importing Libraries
import matplotlib.pyplot as plt

T = 100.0                               #Max iteration value
dt = 0.01                               #Step size
N = np.int(T/dt)+1                      #Converts T/dt into an integer for linspace
t1 = np.linspace(0.0,T,N)               #Creates an array from 0.0 to T
t = np.arange(0.0,T+dt,dt)              #Creates same array from 0.0 to T

