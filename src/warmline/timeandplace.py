import pandas as pd
import os
import matplotlib.pyplot as plt
import numpy as np
#files = pd.read_csv("data/01-24.csv")
pd.DataFrame()

from head import df

df["Zip"] = df["Zip"].astype(float).astype(int)

#d = df[df["Age"] > df["Age"].quantile(0.5) ]

d = df["Zip"].value_counts()[df["Zip"].value_counts().values > 3]
df = pd.DataFrame({
    "Zip": d.index,
    "Val": d.values
})
print(df.plot.bar(x='Zip', y='Val', rot=0, color="red", figsize=(20, 10)))


from func import save
save(__file__)