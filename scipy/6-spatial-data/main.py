import numpy as np
from scipy.spatial import Delaunay  
from scipy.spatial import ConvexHull
from scipy.spatial import KDTree
from scipy.spatial.distance import euclidean
from scipy.spatial.distance import cityblock
from scipy.spatial.distance import cosine
from scipy.spatial.distance import hamming
import matplotlib.pyplot as plt

points = np.array([
    [2, 4],
    [3, 4],
    [3, 0],
    [2, 2],
    [4, 1]
])

simplices = Delaunay(points).simplices

print(simplices)


plt.triplot(points[:, 0], points[:, 1], simplices)
plt.scatter(points[:, 0], points[:, 1], color='r')

plt.show()

# -------------------------------- convex hull ------------------------------- #

points = np.array([
    [2, 4],
    [3, 4],
    [3, 0],
    [2, 2],
    [4, 1],
    [1, 2],
    [5, 0],
    [3, 1],
    [1, 2],
    [0, 2]
])

hull_points = ConvexHull(points).simplices

plt.scatter(points[:,0], points[:,1])
for simplex in hull_points:
  plt.plot(points[simplex,0], points[simplex,1], 'k-')

plt.show()

# ---------------------------------- kdtrees --------------------------------- #

points = [(1, -1), (2, 3), (-2, 3), (2, -3)]

kdtree = KDTree(points)

print(kdtree.query((1, 1)))

# ---------------------------- euclidean distance ---------------------------- #

p1 = (1, 0)
p2 = (10, 2)

print(euclidean(p1, p2))

# ------------------ cityblock distance (manhattan distance) ----------------- #

p1 = (1, 0)
p2 = (10, 2)

print(cityblock(p1, p2))

# ------------------------------ cosine distance ----------------------------- #

p1 = (1, 0)
p2 = (10, 2)

print(cosine(p1, p2))

# ----------------------------- hamming distance ----------------------------- #

p1 = (True, False, True)
p2 = (False, True, True)

print(hamming(p1, p2))
