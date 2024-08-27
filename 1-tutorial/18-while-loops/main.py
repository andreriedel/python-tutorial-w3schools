i = 0
while i < 6:
    print(i, end=' ') # change the final character (default is \n)
    i += 1

print() # break line

# ----------------------------------- break ---------------------------------- #

i = 0
while i < 6:
    print(i, end=' ')
    if i == 3:
        break
    i += 1

print() # break line

# --------------------------------- continue --------------------------------- #

i = 0
while i < 6:
    i += 1
    if i == 3:
        continue
    print(i, end=' ')

print() # break line

# ------------------------------ else statement ------------------------------ #

i = 0
while i < 6:
    print(i , end=' ')
    i += 1
else:
    print('\ni is no longer less than 6')
