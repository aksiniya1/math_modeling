from sympy import symbols, diff, cos, sin, tan, log, exp, simplify, pprint

x = symbols('x')

functions = {
    'cos^5(x)':       cos(x)**5,
    'sin(x)':         sin(x),
    'tan(x)':         tan(x),         # tg
    'lg(x) = log10(x)': log(x, 10),   # десятичный логарифм
    'e^x':            exp(x),
    'x^2':            x**2,
    '3x^2 - 5 sin(4x)': 3*x**2 - 5*sin(4*x)
}

for name, f in functions.items():
    df = simplify(diff(f, x))
    print(f"{name} ->")
    pprint(df)
    print()
