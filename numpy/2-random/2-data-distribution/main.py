from numpy import random as rd

# p: probability
x = rd.choice([3, 5, 7, 9], p=[0.1, 0.3, 0.6, 0.0], size=(100))

print(x)
