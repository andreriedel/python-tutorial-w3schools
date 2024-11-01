import numpy as np

arr = np.array([1, 2, 3, 4])
print(arr[0])

# ----------------------------- access 2-D arrays ---------------------------- #

arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])
print(arr[0, 1])

# ----------------------------- access 3-D arrays ---------------------------- #

arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
print(arr[0, 1, 2])

# ----------------------------- negative indexing ---------------------------- #

arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])
print(arr[0, -1]) # access the last column
