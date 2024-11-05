import matplotlib.pyplot as plt
import numpy as np

# --------------------------- title and super title -------------------------- #

#plot 1:
x = np.array([0, 1, 2, 3])
y = np.array([3, 8, 1, 10])

plt.subplot(1, 2, 1)
plt.title("SALES")
plt.plot(x,y)

#plot 2:
x = np.array([0, 1, 2, 3])
y = np.array([10, 20, 30, 40])

plt.subplot(1, 2, 2)
plt.title("INCOME")
plt.plot(x,y)

plt.suptitle("MY SHOP")
plt.show()
