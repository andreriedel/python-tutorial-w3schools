import matplotlib.pyplot as plt
import numpy as np

ypoints = np.array([3, 8, 1, 10])

# -------------------------------- line style -------------------------------- #

# linestyle or ls
plt.plot(ypoints, ls='dotted')
plt.show()

# using shorter syntax
plt.plot(ypoints, ls='--')
plt.show()

# -------------------------------- line color -------------------------------- #

# color or c
plt.plot(ypoints, c='r')
plt.show()

# -------------------------------- line width -------------------------------- #

# linewidth or lw
plt.plot(ypoints, lw='20')
plt.show()

# ------------------------------ multiple lines ------------------------------ #

y1 = np.array([3, 8, 1, 10])
y2 = np.array([6, 2, 7, 11])

plt.plot(y1)
plt.plot(y2)

plt.show()
