thisdict = {
    'brand': 'Ford',
    'model': 'Mustang',
    'year': 1964
}
thisdict.pop('model')
print(thisdict)

thisdict = {
    'brand': 'Ford',
    'model': 'Mustang',
    'year': 1964
}
thisdict.popitem()  # remove the last item
print(thisdict)

thisdict = {
    'brand': 'Ford',
    'model': 'Mustang',
    'year': 1964
}
del thisdict['model']
print(thisdict)

del thisdict  # delete the entire dictionerie

thisdict = {
    'brand': 'Ford',
    'model': 'Mustang',
    'year': 1964
}
thisdict.clear()
print(thisdict)
