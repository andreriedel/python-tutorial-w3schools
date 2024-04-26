thislist = ['apple', 'banana', 'cherry']

thislist[1] = 'blackcurrant'
print(thislist)

thislist[1:3] = ['kiwi', 'watermelon']
print(thislist)

thislist[1:2] = ['orange', 'mango'] # add new item
print(thislist)

thislist[1:3] = ['banana'] # remove item
print(thislist)

thislist = ['apple', 'banana', 'cherry']
thislist.insert(2, 'watermelon')
print(thislist) 
