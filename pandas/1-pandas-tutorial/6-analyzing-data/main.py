import pandas as pd

df = pd.read_csv('data.csv')

# head: view the first rows
print(df.head(10)) # default 5 rows

print() # break line

# tail: view the las rows
print(df.tail()) # default 5 rows

print() # break line

# ---------------------------------------------------------------------------- #

print(df.info())
