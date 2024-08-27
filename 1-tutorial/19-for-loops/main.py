fruits = ['apple', 'banana', 'cherry']

# ---------------------------- loop through a list --------------------------- #

for x in fruits:
    print(x, end=' ')

print() # break line

# --------------------------- loop through a string -------------------------- #

for x in "banana":
  print(x, end=' ')

print() # break line

# ----------------------------------- break ---------------------------------- #

for x in fruits:
    print(x, end=' ')
    if x == 'banana':
        break

print() # break line

# --------------------------------- continue --------------------------------- #

for x in fruits:
    if x == 'banana':
        continue
    print(x, end=' ')

print() # break line

# ----------------------------------- range ---------------------------------- #

for i in range(6):
    print(i, end=' ')

print() # break line

for i in range(2, 6):
    print(i, end=' ')

print() # break line

for i in range(2, 30, 3):
    print(i, end=' ')

print() # break line

# ------------------------------ else statement ------------------------------ #

for i in range(6):
    print(i, end=' ')
else:
    print('Finally finished!')

print() # break line

for i in range(6):
    if i == 3: break
    print(i, end=' ')
else:
    print('Finally finished!') # not executed

print() # break line

# ------------------------------ pass statement ------------------------------ #

for x in [0, 1, 2]:
    pass
