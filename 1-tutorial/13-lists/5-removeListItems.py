thislist = ['apple', 'banana', 'cherry']
thislist.remove('banana')
print(thislist)

thislist = ['apple', 'banana', 'cherry']
thislist.pop(1)
print(thislist)

thislist = ['apple', 'banana', 'cherry']
fruit = thislist.pop(1)
print(fruit)

thislist = ['apple', 'banana', 'cherry']
fruit = thislist.pop() # remove the last one
print(fruit)

thislist = ['apple', 'banana', 'cherry']

del thislist[0]
print(thislist)

del thislist # delete the entire list
# print(thislist) # error

thislist = ['apple', 'banana', 'cherry']
thislist.clear()
print(thislist)
