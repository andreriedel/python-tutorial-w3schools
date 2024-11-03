from numpy import random as rd

x = rd.randint(100)
print(x)

x = rd.rand() # returns a float between 0 and 1
print(f'{x:.4f}')

print() # break line

# --------------------------- generate random array -------------------------- #

arr = rd.randint(100, size=(5))
print(arr)

arr = rd.randint(100, size=(2, 5))
print(arr)

arr = rd.rand(5)
print(arr)

arr = rd.rand(2, 5)
print(arr)

print() # break line

# --------------------- generate random number from array -------------------- #

arr = rd.choice([3, 4, 7, 9])
print(arr)

arr = rd.choice([3, 4, 7, 9], size=(2, 5))
print(arr)
