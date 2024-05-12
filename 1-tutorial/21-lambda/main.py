sum = lambda a, b: a + b

print(sum(5, 10))

print() # break line

# ---------------------------------------------------------------------------- #

def myfunc(n):
    return lambda a : a * n

mydoubler = myfunc(2)
mytripler = myfunc(3)

print(mydoubler(11))
print(mytripler(11))
