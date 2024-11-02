import numpy as np

arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])

arr3 = np.concatenate([arr1, arr2])
print(arr3)

print() # break line

# ------------------------------ join 2-D arrays ----------------------------- #

arr1 = np.array([[1, 2],
                 [3, 4]])

arr2 = np.array([[5, 6],
                 [7, 8]])

arr3 = np.concatenate([arr1, arr2], axis=0)
print(arr3)

arr4 = np.concatenate([arr1, arr2], axis=1)
print(arr4)

print() # break line

# ------------------- joining arrays using stack functions ------------------- #

arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])

arr3 = np.stack((arr1, arr2), axis=1) # stack alows axis 1 for 1-D arrays
print(arr3)

print() # break line

# ---------------------------- stacking along rows --------------------------- #

arr = np.hstack((arr1, arr2))
print(arr)

print() # break line

# -------------------------- stacking along columns -------------------------- #

arr = np.vstack((arr1, arr2))
print(arr)

print() # break line

# ----------------------- stacking along height (depth) ---------------------- #

arr = np.dstack((arr1, arr2))
print(arr)
