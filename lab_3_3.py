import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

def f(t, y):
    return [y[1], np.sin(t) + np.cos(t)] 

t = np.linspace(-5, 5, 200)
sol = solve_ivp(f, [-5, 5], [3, 0], t_eval=t)

plt.plot(t, sol.y[0], 'b', label='y(t)')
plt.plot(t, sol.y[1], 'r', label="y'(t)")
plt.grid(True)
plt.show()
plt.savefig('fig_4.png')