import numpy as np

arr = np.array([1, 2, 3])

for x in arr:
    print(x)

print() # break line

# --------------------------- iterating 2-D arrays --------------------------- #

arr = np.array([[1, 2, 3],[4, 5, 6]])

for x in arr:
    print(x)

print() # break line

for x in arr:
    for y in x:
        print(y)

print() # break line

# ----------------------- iterating arrays using nditer ---------------------- #

for x in np.nditer(arr):
    print(x)

print() # break line

# ---------------- iterating array with differente data types ---------------- #

arr = np.array([1, 2, 3])

for x in np.nditer(arr, flags=['buffered'], op_dtypes=['S']):
    print(x)

print() # break line

# -------------------- iterating with differente step size ------------------- #

arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])

for x in np.nditer(arr[:, ::2]):
    print(x)

print() # break line

# ----------------- enumerated iteration using ndenumarate() ----------------- #

for idx, x in np.ndenumerate(arr):
    print(idx, x)
