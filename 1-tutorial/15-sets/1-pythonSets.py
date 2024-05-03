# Set items are unordered, unchangeable, and do not allow duplicate values.
# Once a set is created, you cannot change its items, but you can remove items and add new items.

thisset = {'apple', 'banana', 'cherry', 'apple'}
print(thisset)

thisset = {'apple', 'banana', 'cherry', True, 1, 2} # True and 1 are considered the same
print(thisset)

print(len(thisset))
print(type(thisset))

thisset = set(('apple', 'banana', 'cherry'))
print(thisset)
