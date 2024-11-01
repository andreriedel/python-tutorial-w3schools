import numpy as np

arr = np.array([0, 1, 2, 3, 4])

x = arr.copy()
arr[0] = 10

print(arr)
print(x)

# ---------------------------------------------------------------------------- #

y = arr.view()
arr[0] = 20

print(arr)
print(y)

# ---------------------------------------------------------------------------- #

print(x.base)
print(y.base)
