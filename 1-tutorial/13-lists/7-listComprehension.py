fruits = ['apple', 'banana', 'cherry', 'kiwi', 'mango']

# newlist = [expression for item in iterable if condition == True]
# LINK https://www.w3schools.com/python/python_lists_comprehension.asp
newlist = [x for x in fruits if 'a' in x]
print(newlist)

# list comprehension with ternary condition
newlist = [x if x != 'banana' else 'orange' for x in fruits]
print(newlist)
