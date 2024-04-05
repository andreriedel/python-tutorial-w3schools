x = str('Hello World!') # str
x = 'Hello World!' # str
print(x, type(x))

x = int(20) # int
x = 20 # int
print(x, type(x))

x = float(20.5) # float
x = 20.5 # float
print(x, type(x))

x = complex(1j) # complex
x = 1j # complex
print(x, type(x))

x = list(('apple', 'banana', 'cherry')) # list
x = ['apple', 'banana', 'cherry'] # list
print(x, type(x))


x = tuple(('apple', 'banana', 'cherry')) # tuples
x = ('apple', 'banana', 'cherry') # tuple
print(x, type(x))

x = range(6) # range
print(x, type(x))

x = dict(name='John', age=36) # dict
x = {
    'name': 'John',
    'age': 36
} # dict
print(x, type(x))

x = set(('apple', 'banana', 'cherry')) # set
x = {'apple', 'banana', 'cherry'} # set
print(x, type(x))

x = frozenset(('apple', 'banana', 'cherry')) # frozenset
print(x, type(x))

x = True # bool
x = bool(1) # bool
print(x, type(x))

x = b'Hello' # bytes
x = bytes(5) # bytes
print(x, type(x))

x = bytearray(5) # bytearray
print(x, type(x))

x = memoryview(bytes(5)) # memoryview
print(x, type(x))

x = None # NoneType
print(x, type(x))
