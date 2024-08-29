import json

# JSON string
x = '{ "name":"John", "age":30, "city":"New York" }'

y = json.loads(x) # convert into dict
print(y) # python dictionary

# ---------------------------------------------------------------------------- #

 # python dictionary
x = {
    "name": "John",
    "age": 30,
    "city": "New York"
}

y = json.dumps(x) # convert into JSON
print(y) # JSON string

print()  # break line

# ---------------------------------------------------------------------------- #

print(json.dumps({"name": "John", "age": 30}))
print(json.dumps(["apple", "bananas"]))
print(json.dumps(("apple", "bananas")))
print(json.dumps("hello"))
print(json.dumps(42))
print(json.dumps(31.76))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))

print()  # break line

# ---------------------------------------------------------------------------- #

x = {
    "name": "John",
    "age": 30,
    "married": True,
    "divorced": False,
    "children": ("Ann", "Billy"),
    "pets": None,
    "cars": [
        {"model": "BMW 230", "mpg": 27.5},
        {"model": "Ford Edge", "mpg": 24.1}
    ]
}

y = json.dumps(x)
print(y)

print() # break line

# ---------------------------------------------------------------------------- #

y = json.dumps(x, indent=4, separators=(". ", " = "))
print(y)

print() # break line

# ---------------------------------------------------------------------------- #

y = json.dumps(x, indent=4, sort_keys=True)

print(y)
