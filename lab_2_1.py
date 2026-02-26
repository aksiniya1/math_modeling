import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
from scipy.optimize import fsolve

def analytic_solution(t, N0, k):
    """Аналитическое решение N(t) = N0 * exp(k*t)"""
    return N0 * np.exp(k * t)

k = 0.5  
N0 = 100  

t_10 = np.log(10) / k
print(f"Время увеличения в 10 раз при k={k}: {t_10:.4f} ед. времени")

def bacteria_model(N, t, k):
    """Правая часть ДУ: dN/dt = k*N"""
    return k * N

t = np.linspace(0, 10, 100)
N_numeric = odeint(bacteria_model, N0, t, args=(k,)).flatten()
N_analytic = analytic_solution(t, N0, k)

print(f"Численное решение при t={t_10}: {odeint(bacteria_model, N0, [t_10], args=(k,))[0,0]:.2f}")
print(f"Аналитическое решение при t={t_10}: {analytic_solution(t_10, N0, k):.2f}")
print(f"Отношение N/N0: {analytic_solution(t_10, N0, k)/N0:.2f}")

plt.figure(figsize=(10, 6))
plt.plot(t, N_numeric, 'b-', label='Численное решение', linewidth=2)
plt.plot(t, N_analytic, 'r--', label='Аналитическое решение', alpha=0.7)
plt.axvline(x=t_10, color='g', linestyle=':', label=f't = {t_10:.2f} (10x рост)')
plt.axhline(y=N0*10, color='g', linestyle=':', alpha=0.5)

plt.xlabel('Время')
plt.ylabel('Количество бактерий')
plt.title(f'Рост популяции бактерий: dN/dt = {k}·N, N(0) = {N0}')
plt.legend()
plt.grid(True, alpha=0.3)
plt.show()

def time_to_multiply(factor, k):
    """Время для увеличения в factor раз"""
    return np.log(factor) / k

print("\nВремя увеличения в 10 раз для разных k:")
for k_test in [0.1, 0.25, 0.5, 0.75, 1.0]:
    t_test = time_to_multiply(10, k_test)
    print(f"k = {k_test:.2f}: t = {t_test:.4f}")

print("\n" + "="*50)
print("АНАЛИТИЧЕСКОЕ РЕШЕНИЕ ЗАДАЧИ №1")
print("="*50)
print("Дифференциальное уравнение: dN/dt = k·N")
print("Начальное условие: N(0) = N₀")
print("\nРешение:")
print("1. Разделяем переменные: dN/N = k·dt")
print("2. Интегрируем: ∫dN/N = ∫k·dt")
print("3. Получаем: ln|N| = k·t + C")
print("4. Потенцируем: N = e^(k·t + C) = C₁·e^(k·t)")
print("5. Используем N(0) = N₀: N₀ = C₁·e^0 = C₁")
print("6. Окончательно: N(t) = N₀·e^(k·t)")
print("\nВремя увеличения в 10 раз:")
print("N(t)/N₀ = e^(k·t) = 10")
print("k·t = ln(10)")
print("t₁₀ = ln(10)/k ≈ 2.3026/k")