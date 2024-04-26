thislist = ['orange', 'mango', 'kiwi', 'pineapple', 'banana']
thislist.sort() # alphanumerically, ascending, by default
print(thislist)

thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist)

thislist = ['orange', 'mango', 'kiwi', 'pineapple', 'banana']
thislist.sort(reverse=True)
print(thislist)

print() # break line

# ---------------------------------------------------------------------------- #

def myfunc(n):
    return abs(n - 50) # return the absolute value

thislist = [100, 50, 65, 82, 23]
thislist.sort(key=myfunc)
print(thislist)

thislist = ['banana', 'Orange', 'Kiwi', 'cherry']

thislist.sort() # case sensitive by default
print(thislist)

thislist.sort(key=str.lower) # case insensitive
print(thislist)

thislist.reverse()
print(thislist)
