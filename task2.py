from sympy import symbols
from sympy import sqrt
from sympy import simplify

a = symbols('a')

simp_expr = simplify(sqrt(a) - (a / sqrt(a) + 1) * ((a-1) / sqrt(a)))

print(simp_expr)