import pandas as pd

a = [1, 7, 2]

myvar = pd.Series(a)

print(myvar)
print(myvar[0])

print() # break line

# ------------------------------- create labels ------------------------------ #

myvar = pd.Series(a, index=["x", "y", "z"])

print(myvar)
print(myvar["y"])

print() # break line

# ------------------------ key/value objects as series ----------------------- #

calories = {"day1": 420, "day2": 380, "day3": 390}

myvar = pd.Series(calories)

print(myvar)

print() # break line

# ---------------------------------------------------------------------------- #

myvar = pd.Series(calories, index = ["day1", "day2"])

print(myvar)

print() # break line

# --------------------------------- DataFrame -------------------------------- #

data = {
    "calories": [420, 380, 390],
    "duration": [50, 40, 45]
}

myvar = pd.DataFrame(data)

print(myvar)
