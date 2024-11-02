import numpy as np

arr = np.array([1, 2, 3, 4, 5, 4, 4])
x = np.where(arr == 4)
print(x)

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
x = np.where(arr % 2 == 0)
print(x)

# ------------------------------- search sorted ------------------------------ #

arr = np.array([6, 7, 8, 9])

x = np.searchsorted(arr, 7) # uses a binary search
print(x)

# starts from the right
x = np.searchsorted(arr, 7, side='right')
print(x)

arr = np.array([1, 3, 5, 7])
x = np.searchsorted(arr, [2, 4, 6]) # multiple values
print(x)
