import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6])

newarr = np.array_split(arr, 3)

print(newarr)

print(newarr[0])
print(newarr[1])
print(newarr[2])

print() # break line

a1, a2, a3 = newarr

print(a1)
print(a2)
print(a3)

print() # break line

# --------------------------- splitting 2-D arrays --------------------------- #

arr = np.array([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12]])

newarr = np.array_split(arr, 3)

print(newarr)

print(newarr[0])
print(newarr[1])
print(newarr[2])

print() # break line

# ---------------------------------------------------------------------------- #

arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])

newarr = np.array_split(arr, 3, axis=1)

print(newarr)

print() # break line

# ---------------------------------- hsplit ---------------------------------- #

newarr = np.hsplit(arr, 3)

print(newarr)

# hsplit, hstack, vsplit, vstack, dsplit, dstack
