quantity = 3
itemno = 567
price = 49

myorder = "I want {0} pieces of item number {1} for {2:.2f} dollars."

print(myorder.format(quantity, itemno, price))

# ---------------------------------------------------------------------------- #

myorder = "I have a {carname}, it is a {model}."
print(myorder.format(carname = "Ford", model = "Mustang"))

# --------------------------------- f-strings -------------------------------- #

price = 59000
txt = f"The price is {price:,} dollars"
print(txt)
