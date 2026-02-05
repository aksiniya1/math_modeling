import sympy as sym
 
x, y, z = sym.symbols('x y z')
 
expr = x**2 - 2
solve_expr = sym.solve(expr, x)
print(solve_expr)
 
expr = sym.Eq(x, y)
print(expr)
 
expr = sym.Eq(3, 1)
print(expr)
 
expr = sym.Eq(3, 3)
print(expr)
 
solve_expr = sym.solveset(x**2 - 2, x)
print(solve_expr)
 
expr = sym.sin(x**2) - sym.exp(-2*x) + sym.cos(sym.pi / x)
solve_expr = sym.solveset(expr, x)
print(solve_expr)
 
system = [x + y + z - 1, x + y + 2*z - 3, x - 2*y + z]
solve_system = sym.linsolve(system, (x, y, z))
print(solve_system)
 
system = [x**2 + x, x - y]
solve_system = sym.nonlinsolve(system, [x, y])
print(solve_system)
 
system = [x**2 + 1, y**2 + 1]
solve_system = sym.nonlinsolve(system, [x, y])
print(solve_system)
 
system = [x**2 - 2*y**2 -2, x*y - 2]
solve_system = sym.nonlinsolve(system, [x, y])
print(solve_system)