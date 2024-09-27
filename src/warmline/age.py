import pandas as pd
import os
import matplotlib.pyplot as plt
import numpy as np
files = pd.read_csv("data/01-24.csv")


df = pd.concat( [  pd.read_csv(os.path.join(os.path.abspath("."), "data", "warmline", file)).dropna(axis="columns", how="all").dropna(axis="index") for file in list(os.walk("data/warmline"))[0][2]])
def retain_quantile(df, percentile=0.95):
    percentile_val = df['Age'].quantile(percentile)

    return df[df['Age'] <= percentile_val]
#df = pd.read_csv(os.path.join(os.path.abspath("."), "data", "warmline", "05-24.csv"), index_col="Date").dropna(axis="index")

df["YOB"] = df["YOB"].astype(str).replace(" ", "").replace("", 0)
df["Age"] = 2024 - df["YOB"].astype(float).astype(int)
#df["Age"] = 2024 - df["YOB"].astype(int)


#print(df['YOB'].astype(int))
#df['Age'] = 2024 - df['YOB']


#d = df[df['YOB'].astype(str).str.contains(" ") == False].dropna(subset=["Date", "YOB", "Gender"])
#d["Age"] = 2024 - d.astype(int)["YOB"]

# Who's Using
#print(df["Age"])


d = df[df["Age"] > df["Age"].quantile(0.5) ]
d = d[d["Age"] <= d["Age"].quantile(0.95)]



plot = d[["Age", "Gender"]].groupby("Gender").boxplot()

plt.savefig("images/WhoIsUsing.png")
