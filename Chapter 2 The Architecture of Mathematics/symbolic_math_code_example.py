from sympy import symbols, Eq, solve

x, y = symbols('x y')
eq1 = Eq(2*x + 3*y, 6)
eq2 = Eq(-x + y, 1)

solution = solve((eq1, eq2), (x, y))
print(solution)