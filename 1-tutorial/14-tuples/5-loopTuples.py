thistuple = ('apple', 'banana', 'cherry')

for x in thistuple:
    print(x)

print()

for i in range(len(thistuple)):
    print(thistuple[i])

print()

i = 0
while i < len(thistuple):
    print(thistuple[i])
    i = i + 1

print()

[print(x) for x in thistuple]
