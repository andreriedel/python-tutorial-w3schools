import pandas as pd

df = pd.read_csv('data.csv')

df.loc[7, 'Duration'] = 45

print(df.to_string())

# ---------------------------------------------------------------------------- #

for x in df.index:
    if df.loc[x, "Duration"] > 120:
        df.loc[x, "Duration"] = 120
        
# ------------------------------- removing rows ------------------------------ #

for x in df.index:
    if df.loc[x, "Duration"] > 120:
        df.drop(x, inplace=True)
