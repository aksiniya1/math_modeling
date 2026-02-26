import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

def f(t, y):
    return [y[1], -4*y[1] - 5*y[0]]  

t = np.linspace(-5, 5, 300)
sol = solve_ivp(f, [-5, 5], [4, -1], t_eval=t)

plt.plot(t, sol.y[0], 'b', label='y(t)')
plt.plot(t, sol.y[1], 'r', label="y'(t)")
plt.grid(True)
plt.show()
plt.savefig('fig_5.png')