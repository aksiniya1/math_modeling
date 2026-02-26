import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

g = 9.8
m = 0.5 

v0 = 20  

mu = 0.6 / (m * 1)  

def model_a(t, yv):  
    y, v = yv
    return [v, -g - mu * v]

def model_b(t, yv):  
    y, v = yv
    return [v, -g - np.sign(v) * v**2]

t = np.linspace(0, 3, 200)
sol_a = solve_ivp(model_a, [0, 3], [y0, v0], t_eval=t)
sol_b = solve_ivp(model_b, [0, 3], [y0, v0], t_eval=t)

y_ideal = y0 + v0 * t - 0.5 * g * t**2
v_ideal = v0 - g * t

h_max_a = max(sol_a.y[0])
h_max_b = max(sol_b.y[0])
h_ideal = v0**2/(2*g)

plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
plt.legend()
plt.grid(True)

plt.subplot(1, 2, 2)
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.show()
plt.savefig('fig_6.png')

v0_2 = 15  
angle = np.radians(30)
vx0 = v0_2 * np.cos(angle)
vy0 = v0_2 * np.sin(angle)

F_wind = 5  
ax_wind = F_wind / m  

def model_2(t, state):
    x, y, vx, vy = state
    return [vx, vy, ax_wind - mu * vx, -g - mu * vy]


t2 = np.linspace(0, 3, 200)
sol2 = solve_ivp(model_2, [0, 3], [0, 0, vx0, vy0], t_eval=t2)

y_vals = sol2.y[1]
for i in range(1, len(y_vals)):
    if y_vals[i-1] > 0 and y_vals[i] <= 0:
        t_land = sol2.t[i]
        x_land = sol2.y[0][i]


t_ideal = 2 * vy0 / g
x_ideal = vx0 * t_ideal


plt.figure(figsize=(15, 5))

plt.subplot(1, 3, 1)
plt.legend()
plt.grid(True)
plt.axis('equal')

plt.subplot(1, 3, 2)
plt.plot(sol2.t, sol2.y[0], 'r-', label='x(t)')
plt.plot(sol2.t, sol2.y[1], 'b-', label='y(t)')
plt.legend()
plt.grid(True)

plt.subplot(1, 3, 3)
plt.plot(sol2.t, sol2.y[2], 'r-', label='vx')
plt.plot(sol2.t, sol2.y[3], 'b-', label='vy')
v_total = np.sqrt(sol2.y[2]**2 + sol2.y[3]**2)
plt.plot(sol2.t, v_total, 'g-', label='|v|')
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.show()
plt.savefig('fig_7.png')