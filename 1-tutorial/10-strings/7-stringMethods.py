str = "Eu nisi laboris dolor do aliqua exercitation"

print(len(str))
print(str.capitalize()) # capitalize
print(str.casefold()) # lower case
print(str.lower()) # lower case
print(str.upper()) # upper case
print(str.center(50, "-"))
print(str.ljust(50, "-"))
print(str.rjust(50, "-"))
print(str.count("nisi")) 
print(str.startswith("Eu")) # return bool
print(str.endswith(".")) # return bool
print(str.find("dolor")) # return int (index)
print(str.rfind("dolor")) # return int (index); return the last occurance
print(str.index("dolor")) # return int (index)
print(str.rindex("dolor")) # return int (index); return the last occurance
print("For only {price:.2f} dollars!".format(price=49))
print(str.isalnum()) # check if is alphanumeric; return bool
print(str.isalpha()) # check if is alphabetic; return bool
print(str.isascii()) # return bool
print("123".isdecimal()) # return bool
print("123".isdigit()) # return bool
print("2demo".isidentifier()) # check if is an identifier; return bool
print(str.islower()) # return bool
print(str.isupper()) # return bool
print("123".isnumeric()) # return bool
print(str.isprintable()) # return bool
print(str.isspace()) # return bool
print("Hello, And Welcome To My World!".istitle()) # return bool
print("-".join(["John", "Peter", "Vicky"]))
print("     Hello World!     ".strip(), "lorem")
print("     Hello World!     ".lstrip(), "lorem")
print("     Hello World!     ".rstrip(), "lorem")
print(str.replace("dolor", "lorem"))
print()
print(str.split())
print("Thank you for the music\nWelcome to the jungle".splitlines())
print(str.swapcase())
print(str.title())
