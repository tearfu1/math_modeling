from sympy import symbols
from sympy import solveset
from sympy import sin
#Первая часть
x, E, n, M  = symbols('x E n M')

expr = x**2 + x + 1/x + 1/x**2 -4
solve_expr = solveset(expr, x)
print(solve_expr)

#Вторая часть

M = 0.1
n = 0.8
expr = E - n*sin(E-M)
solve_expr = solveset(expr, E)
print(solve_expr)