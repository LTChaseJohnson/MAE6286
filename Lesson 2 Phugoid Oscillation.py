import numpy as np                    #Importing Libraries
import matplotlib.pyplot as plt

T = 100.0                               #Max iteration value
dt = input('Enter step size: ')         #Step size
N = np.int(T/dt)+1                      #Converts T/dt into an integer for linspace
t1 = np.linspace(0.0,T,N)               #Creates an array from 0.0 to T
t = np.arange(0.0,T+dt,dt)              #Creates same array from 0.0 to T
S = np.size(t)

#Initial Conditions
z0 = input('Enter initial altitude: ')     #Initial altitude
v = input('Enter perturbation velocity: ') #Initial perturbation velocity
zt = 100.                                  #Trim altitude
g = 9.81                                   #Acceleration

u = np.array([z0,v])                    #Creates initial condition vector

z = np.zeros(S)                         #Creates an empty vector to store values
z[0] = z0                               #Sets initial height condition

#Steppin' with Euler!
for n in range(1,S):
    u = u + dt*np.array([u[1],g*(1-u[0]/zt)])
    z[n] = u[0]

#Exact solution!
z_e= v*(zt/g)**.5*np.sin((g/zt)**.5*t)+(z0-zt)*np.cos((g/zt)**.5*t)+zt

plt.figure(figsize=(10,4))
plt.ylim(40,160)
plt.xlabel('t',fontsize=14)
plt.ylabel('z',fontsize=14)
plt.plot(t,z)
plt.plot(t,z_e)
plt.legend(['Numerical Solution','Analytical Solution'])
plt.title('step size = %s' %dt)

dt_values = np.array([0.1,0.05,0.01,0.005,0.001,0.0001])
z_values = np.empty_like(dt_values, dtype=np.ndarray)

for i, dt in enumerate(dt_values):     #I have no idea what this does!!           
    N = int(T/dt)+1
    t = np.linspace(0.0,T,N)
    u = np.array([z0,v])
    z = np.empty_like(t)
    z[0] = z0
    
    for n in range(1,N):
        u = u + dt*np.array([u[1], g*(1-u[0]/zt)])
        z[n] = u[0]
        
    z_values[i] = z.copy()

def get_error(z,dt):
    N = len(z)
    t = np.linspace(0.0,T,N)
    z_exact = v*(zt/g)**.5*np.sin((g/zt)**.5*t)+(z0-zt)*np.cos((g/zt)**.5*t)+zt
    return dt*np.sum(np.abs(z-z_exact))
    
error_values = np.empty_like(dt_values)
for i, dt in enumerate(dt_values):
    error_values[i] = get_error(z_values[i],dt)

plt.figure(figsize=(10,4))
plt.grid(True)
plt.xlabel('$\Delta t$', fontsize = 16)
plt.ylabel('Error', fontsize =16)
plt.loglog(dt_values, error_values, 'ko-')
plt.axis('equal')

plt.show()