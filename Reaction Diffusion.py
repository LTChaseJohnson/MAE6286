import numpy
import matplotlib.pyplot as plt
import matplotlib.cm as cm

n = 192

Du, Dv, F, k = 0.00016, 0.00008, 0.035, 0.065 # Bacteria 1 

dh = 5./(n-1)

T = 8000

dt = .9 * dh**2 / (4*max(Du,Dv))

nt = int(T/dt)

uvinitial = numpy.load('C:/Users/DCUnited/Downloads/uvinitial.npz')
U = uvinitial['U']
V = uvinitial['V']

fig = plt.figure(figsize=(8,5))
plt.subplot(121)
plt.imshow(U, cmap = cm.RdBu)
plt.xticks([]), plt.yticks([]);
plt.subplot(122)
plt.imshow(V, cmap = cm.RdBu)
plt.xticks([]), plt.yticks([]);


for n in range(nt):
    un = U.copy()
    vn = V.copy()
    
    U[1:-1,1:-1] = un[1:-1,1:-1]\
    +Du*dt/dh**2*(un[2:,1:-1]+un[:-2,1:-1]+un[1:-1,2:]+un[1:-1,:-2]-4.*un[1:-1,1:-1])\
    -dt*(un[1:-1,1:-1]*vn[1:-1,1:-1]**2)+dt*F*(1-un[1:-1,1:-1])
    V[1:-1,1:-1] = vn[1:-1,1:-1]\
    +Dv*dt/dh**2*(vn[2:,1:-1]+vn[:-2,1:-1]+vn[1:-1,2:]+vn[1:-1,:-2]-4.*vn[1:-1,1:-1])\
    +dt*(un[1:-1,1:-1]*vn[1:-1,1:-1]**2)-dt*vn[1:-1,1:-1]*(F+k)
    
    #Neumann BCs are all zero
    U[-1,:] = U[-2,:]
    U[:,-1] = U[:,-2]
    U[0,:] = U[1,:]
    U[:,0] = U[:,1]
    
    V[-1,:] = V[-2,:]
    V[:,-1] = V[:,-2]
    V[0,:] = V[1,:]
    V[:,0] = V[:,1]

print U[100,::40]
plt.show()