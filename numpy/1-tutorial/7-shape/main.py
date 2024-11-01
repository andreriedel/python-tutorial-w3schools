import numpy as np

arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
print(arr.shape) # tuple with 2 elements (2-D array)

arr = np.array([1, 2, 3, 4], ndmin=5)
print(arr.shape)
