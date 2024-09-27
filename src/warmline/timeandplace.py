import pandas as pd
import os
import matplotlib.pyplot as plt
import numpy as np
#files = pd.read_csv("data/01-24.csv")
pd.DataFrame()

df = pd.concat( [  pd.read_csv(os.path.join(os.path.abspath("."), "data", "warmline", file)).dropna(axis="columns", how="all").dropna(axis="index") for file in list(os.walk("data/warmline"))[0][2]])

df["Zip"] = df["Zip"].astype(float).astype(int)

#d = df[df["Age"] > df["Age"].quantile(0.5) ]

d = df["Zip"].value_counts()[df["Zip"].value_counts().values > 3]
df = pd.DataFrame({
    "Zip": d.index,
    "Val": d.values
})
print(df.plot.bar(x='Zip', y='Val', rot=0, color="red", figsize=(20, 10)))


plt.savefig("images/Zips.png",)