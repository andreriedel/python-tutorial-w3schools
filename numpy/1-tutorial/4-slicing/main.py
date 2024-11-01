import numpy as np

arr = np.array([0, 1, 2, 3, 4, 5])

print(arr[0:4])

print(arr[:4])

print(arr[0:])

print(arr[::2]) # step 2

# ----------------------------- negative slicing ----------------------------- #

print(arr[-3:-1])

# ------------------------------- negative step ------------------------------ #

print(arr[::-1]) # reverse order

# ---------------------------- slicing 2-D arrays ---------------------------- #

arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])

print(arr[1, 0:4])
print(arr[0:2, 2])
print(arr[0:2, 0:4]) # 2-D array
