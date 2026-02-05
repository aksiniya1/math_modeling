import math
print(math.sqrt(3))
 
import sympy as sym
print(sym.sqrt(3))
print(2 * sym.sqrt(3))
 
x, y = sym.symbols('x y')
expr = x + 2*y
print(expr)
print(expr + 1)
print(x * expr)
 
print(sym.sin(x**2) - sym.exp(-2*x) + sym.cos(sym.pi / x))
