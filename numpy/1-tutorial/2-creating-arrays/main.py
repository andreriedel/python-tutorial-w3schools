import numpy as np

arr = np.array([1, 2, 3, 4, 5])

print(arr)
print(type(arr))

print() # break line

# -------------------------------- 0-D arrays -------------------------------- #

arr = np.array(42)
print(arr)
print(arr.ndim)

print() # break line

# -------------------------------- 1-D arrays -------------------------------- #

arr = np.array([1, 2, 3, 4, 5])
print(arr)
print(arr.ndim)

print() # break line

# -------------------------------- 2-D arrays -------------------------------- #

arr = np.array([[1, 2, 3], [4, 5, 6]])
print(arr)
print(arr.ndim)

print() # break line

# -------------------------------- 3-D arrays -------------------------------- #

arr = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])
print(arr)
print(arr.ndim)

print() # break line

# ------------------------- higher dimensional arrays ------------------------ #

arr = np.array([1, 2, 3, 4], ndmin=5)

print(arr)
print('number of dimensions :', arr.ndim)
