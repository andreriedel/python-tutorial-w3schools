import mymodule as mm
from platform import system

mm.greeting("Jonathan")

a = mm.person1["age"]
print(a)

x = dir(mm)
print(x)

print(system())
