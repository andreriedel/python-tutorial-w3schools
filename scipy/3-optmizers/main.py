from scipy.optimize import root
from scipy.optimize import minimize
import math

# --------------------------- roots of an equation --------------------------- #

eqn = lambda x: x + math.cos(x)

# 0: initial guess
myroot = root(eqn, 0)

print(myroot)
print(myroot.x)

# ------------------------------ finding minima ------------------------------ #

eqn = lambda x: x**2 + x + 2

# 0: initial guess
mymin = minimize(eqn, 0, method='BFGS')

print(mymin)

# Methods:
# 'CG'
# 'BFGS'
# 'Newton-CG'
# 'L-BFGS-B'
# 'TNC'
# 'COBYLA'
# 'SLSQP'
