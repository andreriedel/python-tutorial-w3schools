from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

"""
lam - rate or known number of occurrences.
size - The shape of the returned array.
"""

x = random.poisson(lam=2, size=10)
print(x)

# ---------------------------------------------------------------------------- #

sns.distplot(random.poisson(lam=2, size=1000), kde=False)
plt.show()
