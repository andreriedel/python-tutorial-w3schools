import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array([1, 8])
ypoints = np.array([3, 10])

plt.plot(xpoints, ypoints)
plt.show()

# --------------------------- plotting without line -------------------------- #

plt.plot(xpoints, ypoints, 'o')
plt.show()

# ------------------------------ multiple points ----------------------------- #

xpoints = np.array([1, 2, 6, 8])
ypoints = np.array([3, 8, 1, 10])

plt.plot(xpoints, ypoints)
plt.show()

# ----------------------------- default x-points ----------------------------- #

ypoints = np.array([3, 8, 1, 10, 5, 7])

plt.plot(ypoints)
plt.show()
