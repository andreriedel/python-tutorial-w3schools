import numpy as np
from scipy.sparse import csr_matrix

arr = np.array([0, 0, 0, 0, 0, 1, 1, 0, 2])

print(csr_matrix(arr))

print() # break line

# --------------------------- sparse matrix methods -------------------------- #

arr = np.array([[0, 0, 0], [0, 0, 1], [1, 0, 2]])

print(csr_matrix(arr).data)
print(csr_matrix(arr).count_nonzero())

print() # break line

# ---------------------------------------------------------------------------- #

mat = csr_matrix(arr)
mat.eliminate_zeros()
print(mat)

print() # break line

# ---------------------------------------------------------------------------- #

mat = csr_matrix(arr)
mat.sum_duplicates()
print(mat)

print() # break line

# ---------------------------------------------------------------------------- #

# converts from csr to csc
newarr = csr_matrix(arr).tocsc()
print(newarr)
