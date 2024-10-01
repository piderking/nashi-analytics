import pandas as pd


df = pd.read_csv("./data/fmt/03-24.csv", index_col=False).dropna(axis="columns", how="all").dropna(axis="index")
dd = pd.read_csv("./data/warmline/02-24.csv", index_col=False).dropna(axis="columns", how="all").dropna(axis="index")


print(df.head())
d = pd.concat([df, dd])

print(d)