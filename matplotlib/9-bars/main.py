import matplotlib.pyplot as plt
import numpy as np

x = np.array(["A", "B", "C", "D"])
y = np.array([3, 8, 1, 10])

plt.bar(x,y)
plt.show()

# ------------------------------ horizontal bars ----------------------------- #

plt.barh(x, y)
plt.show()

# --------------------------------- bar color -------------------------------- #

plt.bar(x, y, color='r')
plt.show()

# --------------------------------- bar width -------------------------------- #

plt.bar(x, y, width=0.1)
plt.show()

# -------------------------------- bar height -------------------------------- #

plt.barh(x, y, height = 0.1)
plt.show()
