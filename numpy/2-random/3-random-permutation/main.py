from numpy import random
import numpy as np

arr = np.array([1, 2, 3, 4, 5])

random.shuffle(arr) # inplace
print(arr)

# ---------------------------------------------------------------------------- #

arr = np.array([1, 2, 3, 4, 5])
print(random.permutation(arr))
