from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

"""
loc - mean, where the peak is. Default 0.

size - The shape of the returned array.
"""

x = random.logistic(loc=1, scale=2, size=(2, 3))
print(x)

# ---------------------------------------------------------------------------- #

sns.distplot(random.logistic(size=1000), hist=False)
plt.show()
