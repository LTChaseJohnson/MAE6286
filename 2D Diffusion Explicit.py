import numpy as np
import matplotlib.pyplot as plt

def ftcs(T,nt,alpha,dt,dx,dy):
    # Defining the midpoint
    jmid = (np.size(T[:,0])+1)/2
    imid = (np.size(T[0,:])+1)/2
    for n in range(nt):
        Tn = T.copy()
        T[1:-1,1:-1] = Tn[1:-1,1:-1] + alpha*dt/dy**2*(Tn[2:,1:-1]-2*Tn[1:-1,1:-1]+Tn[:-2,1:-1])\
        + alpha*dt/dx**2*(Tn[1:-1,2:]-2*Tn[1:-1,1:-1]+Tn[1:-1,:-2])
  
        # Enforce Neumann BCs
        T[-1,:] = T[-2,:]
        T[:,-1] = T[:,-2]
        
        # Check if we reached T=70C
        if T[jmid, imid] >= 70:
            print ("Center of plate reached 70C at time {0:.2f}s.".format(dt*n))
            break
        
    if T[jmid, imid]<70:
        print ("Center has not reached 70C yet, it is only {0:.2f}C.".format(T[jmid, imid]))
        
    return T

L = 1.0E-2
H = 1.0E-2

nx = 21
ny = 21
nt = 500

dx = L/(nx-1)
dy = H/(ny-1)

x = np.linspace(0,L,nx)
y = np.linspace(0,H,ny)

alpha = 1E-4

Ti = np.ones((ny,nx))*20.
Ti[0,:] = 100
Ti[:,0] = 100

sigma = 0.25
dt = sigma*min(dx,dy)**2/alpha
T = Ti.copy()

T = ftcs(T,nt,alpha,dt,dx,dy)

mx,my = np.meshgrid(x,y)
plt.contourf(my,mx,T,20)
plt.colorbar();

plt.show()