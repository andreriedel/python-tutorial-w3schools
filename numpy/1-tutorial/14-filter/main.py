import numpy as np

arr = np.array([41, 42, 43, 44])

filter = [True, False, True, False]
newarr = arr[filter]

print(newarr)

# ------------------------- creating the filter array ------------------------ #

filter = []

for x in arr:
    if x > 42:
        filter.append(True)
    else:
        filter.append(False)

newarr = arr[filter]

print(newarr)

# -------------------- creating filter directly from array ------------------- #

filter = arr > 42
newarr = arr[filter]

print(newarr)
