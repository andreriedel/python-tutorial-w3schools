import pandas as pd

data = {
    "calories": [420, 380, 390],
    "duration": [50, 40, 45]
}

df = pd.DataFrame(data)

print(df)

print() # break line

# -------------------------------- locate row -------------------------------- #

print(df.loc[0])

print() # break line

print(df.loc[[0, 1]])

print() # break line

# ------------------------------- named indexes ------------------------------ #

df = pd.DataFrame(data, index = ["day1", "day2", "day3"])

print(df)

print() # break line

print(df.loc["day1"])

print() # break line

# -------------------------------- load files -------------------------------- #

df = pd.read_csv('data.csv')

print(df) 
