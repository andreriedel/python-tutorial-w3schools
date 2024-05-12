class MyClass:
    x = 5

objetc = MyClass()
print(objetc.x)

print() # break line

# ---------------------------------------------------------------------------- #

class Person:
    # constructor method
    def __init__(self, name, age):
        self.name = name # attribute
        self.age = age # attribute

p1 = Person('John', 36)

print(p1.name)
print(p1.age)

print() # break line

# ---------------------------------------------------------------------------- #

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # used when Person is represented as a string
    def __str__(self):
        return f'{self.name}({self.age})'

p1 = Person('John', 36)

print(p1)

print() # break line

# ---------------------------------------------------------------------------- #

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def myfunc(self):
        print(f'Hello my name is {self.name}, I am {self.age}')

p1 = Person('John', 36)
p1.myfunc()

p1.name = 'André'
p1.age = 21

p1.myfunc()

del p1.age
del p1

class Person:
    pass
