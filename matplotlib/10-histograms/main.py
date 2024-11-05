import matplotlib.pyplot as plt
import numpy as np

# an array with 250 values, where the values will concentrate around 170, and the standard deviation is 10
x = np.random.normal(loc=170, scale=10, size=250)

plt.hist(x)
plt.show() 
