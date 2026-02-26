import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

def system1(x, yz):
    y, z = yz
    dy = y**2
    dz = z / (x + 0.01 - y**2) if abs(x + 0.01 - y**2) > 1e-10 else 0
    return [dy, dz]

x_span = [-5, 5]
sol1 = solve_ivp(system1, x_span, [1, -3], method='RK45', dense_output=True)

x = np.linspace(-5, 5, 200)
y, z = sol1.sol(x)

plt.figure(figsize=(10, 4))
plt.plot(x, y, 'b', label='y(x)')
plt.plot(x, z, 'r', label='z(x)')
plt.grid(True)
plt.savefig('fig_2.png')





def system2(t, xy):
    x, y = xy
    dx = 3*x - 2*y + np.exp(x)/(np.exp(x)+1)
    dy = x - np.exp(-x)/(np.exp(-x)+1)
    return [dx, dy]

t_span = [-1, 1]
sol2 = solve_ivp(system2, t_span, [5, -7], method='RK45', dense_output=True)

t = np.linspace(-1, 1, 200)
x2, y2 = sol2.sol(t)

plt.plot(t, x2, 'b', label='x(t)')
plt.plot(t, y2, 'r', label='y(t)')

plt.figure()
plt.plot(x2, y2, 'g')
plt.plot(x2[0], y2[0], 'ro', label='start')
plt.plot(x2[-1], y2[-1], 'bo', label='end')
plt.grid(True); plt.axis('equal')
plt.show()

plt.savefig('fig_3.png')