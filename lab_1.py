import sympy as sym

x = sym.symbols('x')
expr = sym.sin(x) + sym.log(x, 10) - x
expr_solve = sym.nsolve(expr, 1)
print(expr_solve)


