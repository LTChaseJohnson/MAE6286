import numpy as np
import matplotlib.pyplot as plt

def u_initial(nx,u_max,u_init):
    u = u_max*np.ones(nx)
    u[(nx-1)*2./4:] = u_init
    return u

nx = 81.
u_max = 1.0
u_init = 0.0

u0 = u_initial(nx,u_max,u_init)
x = np.linspace(0,4,nx)

plt.figure(1)
plt.plot(x,u0)
plt.ylim(-0.25,1.25)
plt.title('Initial Velocity')
plt.ylabel(r'$\frac{m}{s}$', size=16)
plt.xlabel(r'$m$', size=16)

plt.show()