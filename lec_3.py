import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt 
	
t = np.arange(0, 10, 0.01)

def diff_func(z, t): 
    theta, omega = z 
    
    dtheta_dt = omega

    domega_dt = - k * omega - c * np.sin(theta)

    return dtheta_dt, domega_dt
     
 

theta0 = np.pi - 0.1
omega0 = 0
 
z0 = theta0, omega0

k = 0.25
c = 5.0
 
sol = odeint(diff_func, z0, t)
 
plt.plot(t, sol[:, 0], 'b', label='theta(t)')
 
plt.legend()
plt.savefig('fig_1.png')
