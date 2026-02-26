import numpy as np
import matplotlib.pyplot as plt

k1 = 0.3  
k2 = 0.2 
A0 = 10   

t = np.linspace(0, 20, 200)

A = A0 * np.exp(-(k1 + k2) * t)
X = A0 * k1/(k1 + k2) * (1 - np.exp(-(k1 + k2) * t))
Y = A0 * k2/(k1 + k2) * (1 - np.exp(-(k1 + k2) * t))

plt.figure(figsize=(10, 4))
plt.subplot(1, 2, 1)
plt.plot(t, A, 'b-', linewidth=2)
plt.plot(t, X, 'g-', linewidth=2)
plt.plot(t, Y, 'orange', linewidth=2)
plt.legend()
plt.grid(True)
plt.subplot(1, 2, 2)
plt.plot(t, X/Y, 'm-', linewidth=2)
plt.axhline(y=k1/k2, color='k', linestyle='--',)
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

plt.savefig('fig_8.png')



m = 0.8     
k = 500     
v0 = 5       
g = 9.8    

x0_eq = m * g / k  

omega = np.sqrt(k/m)  
T = 2 * np.pi / omega  

A_amp = v0 / omega
t = np.linspace(0, 2, 500) 
x = -A_amp * np.sin(omega * t)
v = -A_amp * omega * np.cos(omega * t)
x_total = x0_eq + x
E_kin = 0.5 * m * v**2
E_pot = 0.5 * k * x**2
E_total = E_kin + E_pot

plt.figure(figsize=(15, 5))

plt.subplot(1, 3, 1)
plt.plot(t, x*100, 'b-', label='Смещение (см)')
plt.plot(t, v, 'r-', label='Скорость (м/с)')
plt.legend()
plt.grid(True)
plt.axhline(y=0, color='k', linestyle='-', alpha=0.3)

plt.subplot(1, 3, 2)
plt.plot(t, E_kin, 'g-', alpha=0.7)
plt.plot(t, E_pot, 'b-', alpha=0.7)
plt.plot(t, E_total, 'r-', linewidth=2)
plt.legend()
plt.grid(True)
plt.subplot(1, 3, 3)
plt.plot(x*100, v, 'm-', linewidth=2)
plt.grid(True)
plt.axhline(y=0, color='k', linestyle='-', alpha=0.3)
plt.axvline(x=0, color='k', linestyle='-', alpha=0.3)
plt.axis('equal')
plt.tight_layout()
plt.show()
plt.figure(figsize=(10, 4))
plt.axhline(y=x0_eq*100, color='r', linestyle='--',)
plt.plot(t, x_total*100, 'b-', linewidth=2,)
plt.plot(0, x_total[0]*100, 'ro', markersize=8,)
plt.legend()
plt.grid(True)
plt.show()
plt.savefig('fig_9.png')