import pandas as pd

df = pd.read_csv('data.csv')

print(df.duplicated())

print() # break line

df.drop_duplicates(inplace=True)

print(df.to_string())
