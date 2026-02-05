import sympy as sym
f = sym.Function('f')
x = sym.Function('x')
y = sym.Function('y')
z = sym.Function('z')
	
t = sym.Symbol('t')
R = 1
f = x(t)**2 + y(t)**2 + z(t)**2 - R**2
print(sym.diff(f, x(t)))
 
print(sym.diff(f, y(t)))
 
print(sym.diff(f, z(t)))
 
print(sym.diff(f, t))
 
print(sym.diff(sym.diff(f, t), t))
