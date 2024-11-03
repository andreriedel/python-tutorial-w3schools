import matplotlib.pyplot as plt
import seaborn as sns

# ALERT: deprecated
sns.distplot([0, 1, 2, 3, 4, 5], kde=True)
plt.show()

# ALERT: deprecated
sns.distplot([0, 1, 2, 3, 4, 5], hist=False)
plt.show()

# ---------------------------------------------------------------------------- #

sns.histplot([0, 1, 2, 3, 4, 5], kde=True)
plt.show()

sns.kdeplot([0, 1, 2, 3, 4, 5])
plt.show()
