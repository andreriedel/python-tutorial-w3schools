fruits = ['apple', 'banana', 'cherry']
fruits.append('orange')
print(fruits)

fruits.clear()
print(fruits)

fruits = ['apple', 'banana', 'cherry', 'orange']
x = fruits.copy()
print(x)

print(fruits.count('cherry'))

cars = ['Ford', 'BMW', 'Volvo']
fruits.extend(cars)
print(fruits)

x = fruits.index('cherry')
print(x)

fruits = ['apple', 'banana', 'cherry']
fruits.insert(1, 'orange')
print(fruits)

x = fruits.pop(1)
print(x)

fruits.remove('banana')
print(fruits)

fruits = ['apple', 'banana', 'cherry']
fruits.reverse()
print(fruits)

cars = ['Ford', 'BMW', 'Volvo']
cars.sort()
print(cars)
