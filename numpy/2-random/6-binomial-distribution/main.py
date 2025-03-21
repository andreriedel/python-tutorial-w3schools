from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

"""
n - number of trials.
p - probability of occurence of each trial (e.g. for toss of a coin 0.5 each).
size - The shape of the returned array.
"""

x = random.binomial(n=10, p=0.5, size=10)
print(x)

# ---------------------------------------------------------------------------- #

sns.distplot(random.binomial(n=10, p=0.5, size=1000), kde=False)
plt.show()
