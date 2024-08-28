def my_function():
    print('Hello World!')

my_function()

# From a function's perspective: A parameter is the variable listed inside the
# parentheses in the function definition. An argument is the value that is sent
# to the function when it is called.

def print_name(first_name, last_name): # parameters
    print(first_name, last_name + '.')

print_name('André', 'Riedel') # arguments
print_name('Breno', 'Riedel') # arguments

print() # break line

# ---------------------------- arbitrary arguments --------------------------- #

def print_full_name(*params):
    print(type(params)) # tuple
    print(len(params))
    [print(x) for x in params]
    fn, ln = params[0], params[-1]
    print('My name is', fn, ln)

print_full_name('André', 'Zambroni', 'Riedel')

print() # break line

# ----------------------------- keyword arguments ---------------------------- #

def my_function(child3, child2, child1):
  print('The youngest child is ' + child3)

my_function(child1 = 'Emil', child2 = 'Tobias', child3 = 'Linus')

print() # break line

# ------------------------ arbitrary keyword arguments ----------------------- #

def print_full_name(**params):
    print(type(params))
    print(len(params))
    print(params)
    [print(x) for x in params] # print the keys
    [print(x) for x in params.values()] # print the values
    fn, ln = params['fn'], params['ln']
    print('My name is', fn, ln)

print_full_name(fn = 'André', mn = 'Zambroni', ln = 'Riedel')

print() # break line

# -------------------------- default parameter value ------------------------- #

def print_country(country = 'Norway'):
    print('I am from ' + country)

print_country('Brazil')
print_country()

print() # break line

# ---------------------------- list as an argument --------------------------- #

def print_fruits(fruits):
    for fruit in fruits:
        print(fruit)

fruits = ['apple', 'banana', 'cherry']

print_fruits(fruits)

print() # break line

# ------------------------------- return values ------------------------------ #

def times_5(num = 0):
    return num * 5

print(times_5()) # default 0
print(times_5(1))
print(times_5(2))
print(times_5(3))
print(times_5(4))
print(times_5(5))

print() # break line

# ------------------------------ pass statement ------------------------------ #

def myfunction():
    pass

# ------------------------- positional-only arguments ------------------------ #

def my_function(x, /):
    print(x)

my_function(3)

# -------------------------- keyword-only arguments -------------------------- #

def my_function(*, x):
    print(x)

my_function(x = 3)

# ----------------- combine positional-only and keyword-only ----------------- #

def my_function(a, b, /, *, c, d):
    print(a + b + c + d)

my_function(5, 6, c = 7, d = 8)

print() # break line

# --------------------------------- recursion -------------------------------- #

def fibonacci(n):
    if n == 0:
        return 0
    if n == 2 or n == 1:
        return 1
    
    return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(1))
print(fibonacci(2))
print(fibonacci(5))
print(fibonacci(6))
