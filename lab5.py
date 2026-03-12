import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

G = 6.67e-11  # гравитационная постоянная, м^3/(кг·с^2)
M_sun = 1.98847e30  # масса Солнца, кг
au_to_m = 1.496e11  # астрономическая единица в метрах
day_to_sec = 24 * 3600  # день в секундах
year_to_sec = 365.25 * day_to_sec  # год в секундах

m1 = 1.06 * M_sun  # HD 188753 A (желтый карлик)
m2 = 0.96 * M_sun  # HD 188753 B (оранжевый карлик)
m3 = 0.67 * M_sun  # HD 188753 C (красный карлик)

rA0 = np.array([0.0, 0.0, 0.0])  # A в центре
rB0 = np.array([12.3 * au_to_m, 0.0, 0.0])  # B справа
rC0 = np.array([-12.3 * au_to_m, 0.0, 0.0])  # C слева

vA0 = np.array([0.0, 8435, 0.0])  # скорость A вдоль оси Y
vB0 = np.array([0.0, 24556, 0.0])  # скорость B вдоль оси Y
vC0 = np.array([0.0, 21893, 0.0])  # скорость C вдоль оси Y

t_total = 2 * year_to_sec  # 2 года в секундах
dt = day_to_sec  # шаг 1 день
n_steps = int(t_total / dt) + 1

t_array = np.linspace(0, t_total, n_steps)
r1_array = np.zeros((n_steps, 3))
r2_array = np.zeros((n_steps, 3))
r3_array = np.zeros((n_steps, 3))
v1_array = np.zeros((n_steps, 3))
v2_array = np.zeros((n_steps, 3))
v3_array = np.zeros((n_steps, 3))

r1_array[0] = rA0
r2_array[0] = rB0
r3_array[0] = rC0
v1_array[0] = vA0
v2_array[0] = vB0
v3_array[0] = vC0

for i in range(n_steps - 1):
    # Текущие положения
    r1 = r1_array[i]
    r2 = r2_array[i]
    r3 = r3_array[i]
    
    # Вычисление ускорений
    # Векторы от тела 1 к телам 2 и 3
    r12 = r2 - r1
    r13 = r3 - r1
    # Векторы от тела 2 к телам 1 и 3
    r21 = -r12
    r23 = r3 - r2
    # Векторы от тела 3 к телам 1 и 2
    r31 = -r13
    r32 = -r23

    dist12 = np.linalg.norm(r12)
    dist13 = np.linalg.norm(r13)
    dist23 = np.linalg.norm(r23)
    

    a1 = G * m2 * r12 / dist12**3 + G * m3 * r13 / dist13**3

    a2 = G * m1 * r21 / dist12**3 + G * m3 * r23 / dist23**3

    a3 = G * m1 * r31 / dist13**3 + G * m2 * r32 / dist23**3

    v1_array[i+1] = v1_array[i] + a1 * dt
    v2_array[i+1] = v2_array[i] + a2 * dt
    v3_array[i+1] = v3_array[i] + a3 * dt

    r1_array[i+1] = r1_array[i] + v1_array[i+1] * dt
    r2_array[i+1] = r2_array[i] + v2_array[i+1] * dt
    r3_array[i+1] = r3_array[i] + v3_array[i+1] * dt

r1_au = r1_array / au_to_m
r2_au = r2_array / au_to_m
r3_au = r3_array / au_to_m

fig = plt.figure(figsize=(14, 6))

ax1 = fig.add_subplot(121)
ax1.plot(r1_au[:, 0], r1_au[:, 1], 'y-', label='HD 188753 A', linewidth=1)
ax1.plot(r2_au[:, 0], r2_au[:, 1], 'orange', label='HD 188753 B', linewidth=1)
ax1.plot(r3_au[:, 0], r3_au[:, 1], 'r-', label='HD 188753 C', linewidth=1)
ax1.scatter([0], [0], color='yellow', s=100, marker='*')  # начальное положение A
ax1.scatter([12.3], [0], color='orange', s=80, marker='*')  # начальное положение B
ax1.scatter([-12.3], [0], color='red', s=80, marker='*')  # начальное положение C
ax1.set_xlabel('X (а.е.)')
ax1.set_ylabel('Y (а.е.)')
ax1.set_title('Траектории звезд (XY проекция)')
ax1.legend()
ax1.grid(True)
ax1.axis('equal')

ax2 = fig.add_subplot(122, projection='3d')
ax2.plot(r1_au[:, 0], r1_au[:, 1], r1_au[:, 2], 'y-', label='HD 188753 A', linewidth=1)
ax2.plot(r2_au[:, 0], r2_au[:, 1], r2_au[:, 2], 'orange', label='HD 188753 B', linewidth=1)
ax2.plot(r3_au[:, 0], r3_au[:, 1], r3_au[:, 2], 'r-', label='HD 188753 C', linewidth=1)
ax2.scatter([0], [0], [0], color='yellow', s=100, marker='*')
ax2.scatter([12.3], [0], [0], color='orange', s=80, marker='*')
ax2.scatter([-12.3], [0], [0], color='red', s=80, marker='*')
ax2.set_xlabel('X (а.е.)')
ax2.set_ylabel('Y (а.е.)')
ax2.set_zlabel('Z (а.е.)')
ax2.set_title('Траектории звезд (3D)')
ax2.legend()

plt.tight_layout()
plt.show()

plt.savefig('fig_11.png')