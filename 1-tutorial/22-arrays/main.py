# python does not have built-in support for Arrays, but Python Lists can be
# used instead
# However, to work with arrays in Python you will have to import a library, like the NumPy library.

cars = ["Ford", "Volvo", "BMW"]

print(cars[0])
print(len(cars))

for x in cars:
    print(x)

cars.append("Honda")
print(cars)

cars = ["Ford", "Volvo", "BMW"]
cars.pop(1)
print(cars)


cars = ["Ford", "Volvo", "BMW"]
cars.remove("Volvo")
print(cars)
