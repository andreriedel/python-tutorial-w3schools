print(10 > 9)

# evaluate values
print(bool('Hello')) # True
print(bool('')) # False

print(bool(123)) # True
print(bool(0)) # False

print(bool(['apple', 'cherry', 'banana'])) # True
print(bool([])) # False
print(bool(())) # False
print(bool({})) # False

print(bool(None)) # False

class myclass():
  def __len__(self):
    return 0

myobj = myclass()
print(bool(myobj)) # False
