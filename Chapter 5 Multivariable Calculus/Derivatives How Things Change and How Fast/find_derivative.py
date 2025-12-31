import sympy as sp

x = sp.symbols('x')
f = sp.sin(x)

# Derivative of sin(x)
derivative_of_sin = sp.diff(f, x)

# Evaluate at x = 0.72 and x = 0.66
val = f_prime.subs(x, 0.72).evalf()

print("Derivative of sin(x) at x=0.72:", val)