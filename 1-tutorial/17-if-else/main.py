a = 200
b = 100

if b > a:
    print('b is greater than a')
elif a == b:
    print('a and b are equal')
else:
    print('a is greater than b')

if a > b: print('a is greater than b') # short hand if

print('a is greater than b') if a > b else print('b is greater than a') # short hand if else

# ---------------------------------------------------------------------------- #

a = 200
b = 33
c = 500

if a > b and c > a:
    print('Both conditions are True')

if a > b or a > c:
    print('At least one of the conditions is True')

if not b > a:
    print('b is NOT greater than a')

if b > a:
    pass
