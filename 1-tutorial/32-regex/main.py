import re

txt = "The rain in Spain"

x = re.search("^The.*Spain$", txt)
print(x)

# ---------------------------------------------------------------------------- #

x = re.findall("ai", txt)
print(x)

# ---------------------------------------------------------------------------- #

x = re.split("\s", txt)
print(x)

# ---------------------------------------------------------------------------- #

x = re.sub("\s", " - ", txt)
print(x)

# ------------------------------- match object ------------------------------- #

x = re.search(r"\bS\w+", txt)
print(x.span())
print(x.string)
print(x.group())

