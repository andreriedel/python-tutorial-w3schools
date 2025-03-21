import pandas as pd

# -------------------------------- remove rows ------------------------------- #

df = pd.read_csv('data.csv')

new_df = df.dropna() # returns a new dataframe
# df.dropna(inplace=True) # change the original dataframe

print(new_df.to_string())

print() # break line

# --------------------------- replace empty values --------------------------- #

df = pd.read_csv('data.csv')

df.fillna(130, inplace=True)

print(df.to_string())

print() # break line

# -------------------- replace only for specified columns -------------------- #

df = pd.read_csv('data.csv')

df["Calories"].fillna(130, inplace = True)

print(df.to_string())

print() # break line

# ---------------------------- replace using mean ---------------------------- #

df = pd.read_csv('data.csv')

x = df["Calories"].mean()

df["Calories"].fillna(x, inplace = True)

print(df.to_string())

print() # break line

# --------------------------- replace using median --------------------------- #

df = pd.read_csv('data.csv')

x = df["Calories"].median()

df["Calories"].fillna(x, inplace = True)

print(df.to_string())

print() # break line

# ---------------------------- replace using mode ---------------------------- #

df = pd.read_csv('data.csv')

x = df["Calories"].mode()[0]

df["Calories"].fillna(x, inplace = True)

print(df.to_string())
