import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
 
# Определяем переменную величину
x = np.arange(1, 3, 0.01)
 
 
# Определяем функцию для системы диф. уравнений
def diff_func(z, t): # z - изменяемая величина для системы
    theta, omega = z # Указание изменяемых функций, через z
	
    # Первое уравнение системы
    dtheta_dt = omega
    # Второе уравнение системы
    domega_dt = - k * omega - c * np.sin(theta)
    
    return dtheta_dt, domega_dt
 
 
# Определяем начальные значения и параметры,
# входящие в систему диф. уравнений
y0 = 0.01
omega0 = 0.05

 
# Начальное значение изменяемой величины системы
z0 = y0, omega0
 
k = 0.25
c = 5.0
 
# Решаем систему диф. уравнений
sol = odeint(diff_func, z0, x)
# Строим решение в виде графика
plt.plot(x, sol[:, 0], 'b', label='theta(t)')
 
plt.legend()
plt.savefig('fig_1.png')