import numpy as np
from math import log

arr = np.arange(1, 10) # [1 2 3 4 5 6 7 8 9]
print(np.log2(arr))

# ---------------------------------------------------------------------------- #

arr = np.arange(1, 10)
print(np.log10(arr))

# ---------------------------------------------------------------------------- #

arr = np.arange(1, 10)
print(np.log(arr))

# ---------------------------------------------------------------------------- #

nplog = np.frompyfunc(log, 2, 1)
print(nplog(100, 15))
