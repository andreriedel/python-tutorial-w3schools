# ---------------------------------------------------------------------------- #
#                             ARITHMETIC OPERATORS                             #
# ---------------------------------------------------------------------------- #

x = 11

print(x + 5)
print(x - 5)
print(x * 5)
print(x / 5)
print(20 // 3) # floor division
print(x % 2) # modulus
print(x ** 2) # exponentiation

print() # break line

# ---------------------------------------------------------------------------- #
#                             ASSIGNMENT OPERATORS                             #
# ---------------------------------------------------------------------------- #

a = 11
a += 5
print(a)

b = 11
b -= 5
print(b)

c = 11
c *= 5
print(c)

d = 11
d /= 5
print(d)

e = 11
e //= 5
print(e)

f = 11
f %= 2
print(f)

g = 11
g **= 2
print(g)

print() # break line

# ----------------------- bitwise assignment operators ----------------------- #

and1 = 0b00100110; # binary 38
and2 = 0b00101000; # binary 40
#        --------
#        00100000    binary 32
and1 &= and2
print(and1)

or1 = 0b00100110; # binary 38
or2 = 0b00101000; # binary 40
#        --------
#        00101110   binary 46
or1 |= or2
print(or1)

xor1 = 0b00100110; # binary 38
xor2 = 0b00101000; # binary 40
#        --------
#        00001110   binary 14
xor1 ^= xor2
print(xor1)

rs = 0b0101; # binary 5
#      ----
#      0010    binary 2
rs >>= 1
print(rs);

ls = 0b0101; # binary 5
#      ----
#      1010    binary 10
ls <<= 1
print(ls);

# ---------------------------------------------------------------------------- #
#                             COMPARISON OPERATORS                             #
# ---------------------------------------------------------------------------- #

print(5 == 2)
print(5 != 2)
print(5 > 2)
print(5 < 2)
print(5 >= 2)
print(5 <= 2)

print() # break line

# ---------------------------------------------------------------------------- #
#                               LOGICAL OPERATORS                              #
# ---------------------------------------------------------------------------- #

x = 5
print(x > 0 and x < 10)

print(x > 0 or x < 1)

print(not(x > 0 and x < 10))

print() # break line

# ---------------------------------------------------------------------------- #
#                              IDENTIFY OPERATORS                              #
# ---------------------------------------------------------------------------- #

x = ['apple', 'banana']
y = ['apple', 'banana']
z = x

print(x is z)
print(x is y)
print(x == y) # compare values

print(x is not z)
print(x is not y)
print(x != y) # compare values

print() # break line

# ---------------------------------------------------------------------------- #
#                             MEMBERSHIP OPERATORS                             #
# ---------------------------------------------------------------------------- #

x = ['apple', 'banana']

print('banana' in x)

print('banana' not in x)

print() # break line

# ---------------------------------------------------------------------------- #
#                               BITWISE OPERATORS                              #
# ---------------------------------------------------------------------------- #

and1 = 0b00100110; # binary 38
and2 = 0b00101000; # binary 40
#        --------
#        00100000    binary 32
print(and1 & and2)

or1 = 0b00100110; # binary 38
or2 = 0b00101000; # binary 40
#        --------
#        00101110   binary 46
print(or1 | or2)

xor1 = 0b00100110; # binary 38
xor2 = 0b00101000; # binary 40
#        --------
#        00001110   binary 14
print(xor1 ^ xor2)

nt = 0b00100110 # binary 38
#      --------
#      11011001    binary -39
print(~nt)

rs = 0b0101; # binary 5
#      ----
#      0010    binary 2
print(rs >> 1);

ls = 0b0101; # binary 5
#      ----
#      1010    binary 10
print(ls << 1);
