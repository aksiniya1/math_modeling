import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from scipy.constants import epsilon_0

k = 1 / (4 * np.pi * epsilon_0)  # постоянная Кулона, Н·м²/Кл²
day_to_sec = 24 * 3600  # день в секундах
year_to_sec = 365.25 * day_to_sec  # год в секундах

a = 149e9  # сторона треугольника, м
q = 2e5  # модуль заряда, Кл
m = 1.0  # масса каждого заряда, кг

v2 = 10000  # м/с

h = a * np.sqrt(3) / 2

r1_0 = np.array([-a/2, -h/3, 0.0])  # нижняя левая вершина
r2_0 = np.array([a/2, -h/3, 0.0])   # нижняя правая вершина
r3_0 = np.array([0.0, 2*h/3, 0.0])  # верхняя вершина

q1 = +q
q2 = +q
q3 = -q

v1_0 = np.array([0.0, 0.0, 0.0])
v2_0 = np.array([0.0, v2, 0.0])  
v3_0 = np.array([0.0, 0.0, 0.0])

t_total = 1 * year_to_sec  # 1 год
dt = day_to_sec  # шаг 1 день
n_steps = int(t_total / dt) + 1

t_array = np.linspace(0, t_total, n_steps)
r1_array = np.zeros((n_steps, 3))
r2_array = np.zeros((n_steps, 3))
r3_array = np.zeros((n_steps, 3))
v1_array = np.zeros((n_steps, 3))
v2_array = np.zeros((n_steps, 3))
v3_array = np.zeros((n_steps, 3))

r1_array[0] = r1_0
r2_array[0] = r2_0
r3_array[0] = r3_0
v1_array[0] = v1_0
v2_array[0] = v2_0
v3_array[0] = v3_0

def compute_accelerations(r1, r2, r3, q1, q2, q3, m):
    
    r12 = r2 - r1
    r13 = r3 - r1
    r23 = r3 - r2
    
   
    d12 = np.linalg.norm(r12)
    d13 = np.linalg.norm(r13)
    d23 = np.linalg.norm(r23)
    
    
    if d12 > 0:
        F12 = k * q1 * q2 * r12 / d12**3
    else:
        F12 = np.zeros(3)
    

    if d13 > 0:
        F13 = k * q1 * q3 * r13 / d13**3
    else:
        F13 = np.zeros(3)
    

    if d12 > 0:
        F21 = k * q2 * q1 * (-r12) / d12**3
    else:
        F21 = np.zeros(3)
    

    if d23 > 0:
        F23 = k * q2 * q3 * r23 / d23**3
    else:
        F23 = np.zeros(3)
    
   
    if d13 > 0:
        F31 = k * q3 * q1 * (-r13) / d13**3
    else:
        F31 = np.zeros(3)

    if d23 > 0:
        F32 = k * q3 * q2 * (-r23) / d23**3
    else:
        F32 = np.zeros(3)

    a1 = (F12 + F13) / m
    a2 = (F21 + F23) / m
    a3 = (F31 + F32) / m
    
    return a1, a2, a3


for i in range(n_steps - 1):

    r1 = r1_array[i]
    r2 = r2_array[i]
    r3 = r3_array[i]
    v1 = v1_array[i]
    v2 = v2_array[i]
    v3 = v3_array[i]
    

    a1, a2, a3 = compute_accelerations(r1, r2, r3, q1, q2, q3, m)
    

    v1_half = v1 + 0.5 * a1 * dt
    v2_half = v2 + 0.5 * a2 * dt
    v3_half = v3 + 0.5 * a3 * dt

    r1_new = r1 + v1_half * dt
    r2_new = r2 + v2_half * dt
    r3_new = r3 + v3_half * dt
   
    a1_new, a2_new, a3_new = compute_accelerations(r1_new, r2_new, r3_new, q1, q2, q3, m)

    v1_new = v1_half + 0.5 * a1_new * dt
    v2_new = v2_half + 0.5 * a2_new * dt
    v3_new = v3_half + 0.5 * a3_new * dt

    r1_array[i+1] = r1_new
    r2_array[i+1] = r2_new
    r3_array[i+1] = r3_new
    v1_array[i+1] = v1_new
    v2_array[i+1] = v2_new
    v3_array[i+1] = v3_new

fig = plt.figure(figsize=(16, 8))


ax1 = fig.add_subplot(121)
ax1.plot(r1_array[:, 0], r1_array[:, 1], 'r-', label='+q (заряд 1)', linewidth=1, alpha=0.7)
ax1.plot(r2_array[:, 0], r2_array[:, 1], 'g-', label='+q (заряд 2)', linewidth=1, alpha=0.7)
ax1.plot(r3_array[:, 0], r3_array[:, 1], 'b-', label='-q (заряд 3)', linewidth=1, alpha=0.7)
ax1.scatter([r1_0[0]], [r1_0[1]], color='red', s=100, marker='o', edgecolors='black')
ax1.scatter([r2_0[0]], [r2_0[1]], color='green', s=100, marker='o', edgecolors='black')
ax1.scatter([r3_0[0]], [r3_0[1]], color='blue', s=100, marker='o', edgecolors='black')
ax1.set_xlabel('X (м)')
ax1.set_ylabel('Y (м)')
ax1.set_title('Траектории зарядов (XY проекция)')
ax1.legend()
ax1.grid(True)
ax1.axis('equal')


x_min = min(np.min(r1_array[:, 0]), np.min(r2_array[:, 0]), np.min(r3_array[:, 0]))
x_max = max(np.max(r1_array[:, 0]), np.max(r2_array[:, 0]), np.max(r3_array[:, 0]))
y_min = min(np.min(r1_array[:, 1]), np.min(r2_array[:, 1]), np.min(r3_array[:, 1]))
y_max = max(np.max(r1_array[:, 1]), np.max(r2_array[:, 1]), np.max(r3_array[:, 1]))
padding = 0.1 * max(x_max - x_min, y_max - y_min)
ax1.set_xlim(x_min - padding, x_max + padding)
ax1.set_ylim(y_min - padding, y_max + padding)

ax2 = fig.add_subplot(122, projection='3d')
ax2.plot(r1_array[:, 0], r1_array[:, 1], r1_array[:, 2], 'r-', label='+q (заряд 1)', linewidth=1, alpha=0.7)
ax2.plot(r2_array[:, 0], r2_array[:, 1], r2_array[:, 2], 'g-', label='+q (заряд 2)', linewidth=1, alpha=0.7)
ax2.plot(r3_array[:, 0], r3_array[:, 1], r3_array[:, 2], 'b-', label='-q (заряд 3)', linewidth=1, alpha=0.7)
ax2.scatter([r1_0[0]], [r1_0[1]], [r1_0[2]], color='red', s=100, marker='o')
ax2.scatter([r2_0[0]], [r2_0[1]], [r2_0[2]], color='green', s=100, marker='o')
ax2.scatter([r3_0[0]], [r3_0[1]], [r3_0[2]], color='blue', s=100, marker='o')
ax2.set_xlabel('X (м)')
ax2.set_ylabel('Y (м)')
ax2.set_zlabel('Z (м)')
ax2.set_title('Траектории зарядов (3D)')
ax2.legend()

plt.tight_layout()
plt.show()


def explore_parameters(q_val, v_val, t_years=1, dt_days=1):

    q1_exp = +q_val
    q2_exp = +q_val
    q3_exp = -q_val
    
    v1_exp = np.array([0.0, 0.0, 0.0])
    v2_exp = np.array([0.0, v_val, 0.0])
    v3_exp = np.array([0.0, 0.0, 0.0])

    t_total_exp = t_years * year_to_sec
    dt_exp = dt_days * day_to_sec
    n_steps_exp = int(t_total_exp / dt_exp) + 1

    r1_exp = np.zeros((n_steps_exp, 3))
    r2_exp = np.zeros((n_steps_exp, 3))
    r3_exp = np.zeros((n_steps_exp, 3))
 
    r1_exp[0] = r1_0
    r2_exp[0] = r2_0
    r3_exp[0] = r3_0
    v1 = v1_exp.copy()
    v2 = v2_exp.copy()
    v3 = v3_exp.copy()

    for i in range(n_steps_exp - 1):
        a1, a2, a3 = compute_accelerations(r1_exp[i], r2_exp[i], r3_exp[i], 
                                           q1_exp, q2_exp, q3_exp, m)
        

        v1_half = v1 + 0.5 * a1 * dt_exp
        v2_half = v2 + 0.5 * a2 * dt_exp
        v3_half = v3 + 0.5 * a3 * dt_exp

        r1_new = r1_exp[i] + v1_half * dt_exp
        r2_new = r2_exp[i] + v2_half * dt_exp
        r3_new = r3_exp[i] + v3_half * dt_exp# Новые ускорения
        a1_new, a2_new, a3_new = compute_accelerations(r1_new, r2_new, r3_new,
                                                       q1_exp, q2_exp, q3_exp, m)

        v1 = v1_half + 0.5 * a1_new * dt_exp
        v2 = v2_half + 0.5 * a2_new * dt_exp
        v3 = v3_half + 0.5 * a3_new * dt_exp
        
        r1_exp[i+1] = r1_new
        r2_exp[i+1] = r2_new
        r3_exp[i+1] = r3_new
    

    plt.figure(figsize=(10, 8))
    plt.plot(r1_exp[:, 0], r1_exp[:, 1], 'r-', label='+q (1)', alpha=0.7)
    plt.plot(r2_exp[:, 0], r2_exp[:, 1], 'g-', label='+q (2)', alpha=0.7)
    plt.plot(r3_exp[:, 0], r3_exp[:, 1], 'b-', label='-q (3)', alpha=0.7)
    plt.scatter([r1_0[0]], [r1_0[1]], color='red', s=100, marker='o')
    plt.scatter([r2_0[0]], [r2_0[1]], color='green', s=100, marker='o')
    plt.scatter([r3_0[0]], [r3_0[1]], color='blue', s=100, marker='o')
    plt.xlabel('X (м)')
    plt.ylabel('Y (м)')
    plt.title(f'Траектории: q={q_val:.1e} Кл, v={v_val} м/с')
    plt.legend()
    plt.grid(True)
    plt.axis('equal')
    plt.show()
    plt.savefig('fig_12.png')
    return r1_exp, r2_exp, r3_exp


# Вариант 1: Уменьшенный заряд
explore_parameters(q_val=1e5, v_val=5000, t_years=2)

# Вариант 2: Увеличенная скорость
explore_parameters(q_val=2e5, v_val=20000, t_years=1)
