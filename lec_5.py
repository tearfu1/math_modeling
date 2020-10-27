from sympy import symbols
from sympy.solvers.inequalities import reduce_abs_inequality
from sympy.solvers.inequalities import reduce_rational_inequalities
from sympy import Abs

x, y, z = symbols('x y z')

sol = reduce_abs_inequality(Abs(x - 5) - 3, '<', x)
print(sol)

sol = reduce_rational_inequalities([[y + 2 >0]], y)
print(sol)

sol = reduce_rational_inequalities([[x**2 <= 0]], x)
print(sol)