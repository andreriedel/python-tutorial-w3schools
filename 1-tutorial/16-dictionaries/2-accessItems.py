thisdict = {
    'brand': 'Ford',
    'model': 'Mustang',
    'year': 1964
}

print(thisdict['model'])
print(thisdict.get('model'))

print(thisdict.keys())
print(thisdict.values())
print(thisdict.items())

if 'model' in thisdict:
    print('Yes, model is one of the keys in the thisdict dictionary')
