import sympy as sym
 
x, y, z = sym.symbols('x y z')
expr = sym.sin(x**2) - sym.exp(-2*x) + sym.cos(sym.pi / x)
expr_new = expr.subs(x, y)
print(expr_new)
 
expr_new = expr.subs(x, sym.pi)
print(expr_new)
expr_num = expr_new.evalf()
print(expr_num)
 
expr_new = expr.subs(x, x**2)
print(expr_new)
 
expr = x**3 + 4*x*y - z	
expr_new = expr.subs([(x, 2), (y, 4), (z, 0)])
print(expr_new)