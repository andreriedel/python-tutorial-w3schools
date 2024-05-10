# Dictionaries are ordered*, changeable and do not allow duplicates.

thisdict = {
    'brand': 'Ford',
    'model': 'Mustang',
    'year': 1964
}

print(thisdict)
print(thisdict['brand'])

print(len(thisdict))
print(type(thisdict))

thisdict = dict(name='John', age=36, country='Norway')
print(thisdict)
