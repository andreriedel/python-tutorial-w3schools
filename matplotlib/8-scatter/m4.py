import matplotlib.pyplot as plt
import numpy as np

x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])

# colors = np.array([0, 10, 20, 30, 40, 45, 50, 55, 60, 70, 80, 90, 100])

maxY = y.max()
colors = [];

for val in y:
    colors.append(val * 100 / maxY)

plt.scatter(x, y, c=colors, cmap='viridis')

plt.colorbar()

plt.show()

""" 
You can specify the colormap with the keyword argument cmap with the value of the colormap, in this case 'viridis' which is one of the built-in colormaps available in Matplotlib.

In addition you have to create an array with values (from 0 to 100), one value for each point in the scatter plot:
"""

# LINK: https://www.w3schools.com/python/matplotlib_scatter.asp
