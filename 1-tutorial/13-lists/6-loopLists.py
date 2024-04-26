thislist = ['apple', 'banana', 'cherry']

for x in thislist:
    print(x)

print() # break line

for i in range(len(thislist)):
    print(thislist[i])

print() # break line

i = 0
while i < len(thislist):
    print(thislist[i])
    i = i + 1

print()

[print(x) for x in thislist] # shorthand for (list comprehension)
