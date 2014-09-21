import numpy as np
import matplotlib.pyplot as plt
from math import *

#Constants
ms = 50         #Mass of rocket shell
g = 9.81         #Gravitational acceleration
rho = 1.091     #Air density
r = 0.5         #Cross sectional radius of rocket
A = np.pi*r**2     #Cross sectional area
ve = 325.        #Exhaust speed
Cd = 0.15       #Drag coefficient
mp0 = 100.       #Initial fuel mass
h0 = 0.          #Initial height
v0 = 0.          #Initial velocity

T = 37.33
dt = 0.1
N = int(T/dt)+1
t = np.linspace(0.0,T,N)

mp_dot = np.piecewise(t,[t<5,t>=5],[20,0])  #Defines piecewise function mp_dot
mp = np.piecewise(t,[t<5,t>=5],[lambda t: mp0-20*t, lambda t: 0])


u = np.empty((N,2))
u[0] = np.array([h0,v0])

def f(u):
    h = u[0]
    v = u[1]
    return np.array([v,-g+(mp_dot[n]*ve)/(ms+mp[n])-(rho*A*Cd*v*abs(v))/(2*(ms+mp[n]))])

def euler_step(u, f, dt):
    return u + dt * f(u)

for n in range(N-1):
    u[n+1] = euler_step(u[n],f,dt)
        

h = u[:,0]
v = u[:,1]
tmaxh = np.where(v<=0.00001)[0][1]
tcrash = np.where(h<=0)[0][2]

maxv = max(v)
maxh = max(h)

print 'Fuel Remaining: ',mp[3.2]
print 'Maximum Velocity: ',maxv
print 'Height at max V: ',h[50]
print 'Maximum Height: ',(maxh+1)
print 'Max Height time: ',(tmaxh+1)
print 'Time of Flight: ',tcrash+1./10.
print 'Crash Velocity: ',v[tcrash]



plt.plot(t,h)
plt.plot(t,v)
plt.ylim(-90,1350)
plt.show()