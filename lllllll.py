import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
 
frames = 200
t = np.linspace(0, 5, frames)
 
def move_func(z, t):
    x, vx, y, vy = z
    
    dx_dt = vx
    dvx_dt = 0
    dy_dt = vy
    dvy_dt = - g
    return dx_dt, dvx_dt, dy_dt, dvy_dt
 
g = 9.8
v = 15
alpha = 80 * np.pi / 180
 
x0 = 0
vx0 = v * np.cos(alpha)
y0 = 0
vy0 = v * np.sin(alpha)
 
z0 = x0, vx0, y0, vy0
 
sol = odeint(move_func, z0, t)
 
fig, ax = plt.subplots()
ball, = plt.plot([], [], 'o', color='r')
ball_line, = plt.plot([], [], '-', color='r')
 
 
def animate(i):
    ball.set_data([sol[i][0]], [sol[i][2]])
    ball_line.set_data(sol[:i, 0], sol[:i, 2])
 
 
ani = FuncAnimation(fig, animate, frames=frames, interval=30)
 
edge = 15
ax.set_xlim(0, edge)
ax.set_ylim(0, edge)
	
ani.save('animation_2.gif', writer="pillow")