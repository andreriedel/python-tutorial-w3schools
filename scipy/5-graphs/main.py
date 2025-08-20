import numpy as np
from scipy.sparse.csgraph import connected_components
from scipy.sparse.csgraph import dijkstra
from scipy.sparse.csgraph import floyd_warshall
from scipy.sparse.csgraph import bellman_ford
from scipy.sparse.csgraph import depth_first_order
from scipy.sparse.csgraph import breadth_first_order
from scipy.sparse import csr_matrix

arr = np.array([
    [0, 1, 2],
    [1, 0, 0],
    [2, 0, 0]
])

newarr = csr_matrix(arr)

# --------------------------- connected components --------------------------- #

print(connected_components(newarr))

# --------------------------------- dijkstra --------------------------------- #

"""
return_predecessors: boolean (True to return whole path of traversal otherwise False).
indices: index of the element to return all paths from that element only.
limit: max weight of path.
"""
print(dijkstra(newarr, return_predecessors=True, indices=0))

# ------------------------------ floyd warshall ------------------------------ #

print(floyd_warshall(newarr, return_predecessors=True))

# ------------------------------- bellman ford ------------------------------- #

print(bellman_ford(newarr, return_predecessors=True, indices=0))

print() # break line

# ----------------------------- depth first order ---------------------------- #

arr = np.array([
    [0, 1, 0, 1],
    [1, 1, 1, 1],
    [2, 1, 1, 0],
    [0, 1, 0, 1]
])

newarr = csr_matrix(arr)

print(depth_first_order(newarr, 1))

# ---------------------------- breadth first order --------------------------- #

print(breadth_first_order(newarr, 1))
