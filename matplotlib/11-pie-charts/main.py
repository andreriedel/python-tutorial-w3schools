import matplotlib.pyplot as plt
import numpy as np

y = np.array([35, 25, 25, 15])

plt.pie(y)
plt.show()

# ---------------------------------- labels ---------------------------------- #

mylabels = ["Apples", "Bananas", "Cherries", "Dates"]

plt.pie(y, labels=mylabels)
plt.show() 

# -------------------------------- start angle ------------------------------- #

plt.pie(y, labels=mylabels, startangle=90)
plt.show()

# ---------------------------------- explode --------------------------------- #

myexplode = [0.2, 0, 0, 0]

plt.pie(y, labels=mylabels, explode=myexplode)
plt.show()

# ---------------------------------- shadow ---------------------------------- #

plt.pie(y, labels=mylabels, explode=myexplode, shadow=True)
plt.show()

# ---------------------------------- colors ---------------------------------- #

mycolors = ["black", "hotpink", "b", "#4CAF50"]

plt.pie(y, labels=mylabels, colors=mycolors)
plt.show()

# ---------------------------------- legend ---------------------------------- #

y = np.array([35, 25, 25, 15])
mylabels = ["Apples", "Bananas", "Cherries", "Dates"]

plt.pie(y, labels = mylabels)
plt.legend(title = "Four Fruits:")
plt.show()
