x = ('apple', 'banana', 'cherry')
y = list(x) # convert into a list
y[1] = 'kiwi'
x = tuple(y)

print(x)

thistuple = ('apple', 'banana', 'cherry')
y = ('orange',)
thistuple += y

print(thistuple)

del thistuple
