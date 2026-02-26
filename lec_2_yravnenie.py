import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
t = np.arange(0, 10**6, 100)
def radio_function(m, t):
    dmdt = - k * m
    return dmdt
m_0 = 10
k = 1.61 * 10**(-6)
'''
k_Ur_238 = 4.84*10**(-18) # Уран 238
k_Tl_210 = 8.76*10**(-3) # Талий 210
'''
m_t = odeint(radio_function, m_0, t)
plt.plot(t, m_t[:,0], label='Распад Висмута 210')
plt.xlabel('Период распада, секунды')
plt.ylabel('Функция распада')
plt.title('Радиоактивный распад')
plt.legend()

plt.savefig('fig_1.png')