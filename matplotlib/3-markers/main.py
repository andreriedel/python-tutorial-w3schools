import matplotlib.pyplot as plt
import numpy as np

ypoints = np.array([3, 8, 1, 10])

# marker argument to emphasize each point with a marker
plt.plot(ypoints, marker='o')
plt.show()

# using star marker
plt.plot(ypoints, marker='*')
plt.show()

# ---------------------------- format strings fmt ---------------------------- #
# marker|line|color

plt.plot(ypoints, 'o:b')
plt.show()

# -------------------------------- marker size ------------------------------- #

# markersize or ms
plt.plot(ypoints, marker='o', ms=20)
plt.show()

# ----------------------------- marker edge color ---------------------------- #

# markeredgecolor or mec
plt.plot(ypoints, marker='o', ms=20, mec='r')
plt.show()

# ----------------------------- marker face color ---------------------------- #

# markerfacecolor or mfc
plt.plot(ypoints, marker='o', ms=20, mfc='r')
plt.show()

# --------------------------- heximal color values --------------------------- #

plt.plot(ypoints, marker='o', ms=20, mec='#4CAF50', mfc='#4CAF50')
plt.show()

# you can also use color names
