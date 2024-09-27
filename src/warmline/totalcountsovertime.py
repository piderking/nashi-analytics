import pandas as pd
import os
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

#files = pd.read_csv("data/01-24.csv")
pd.DataFrame()

df = pd.concat( [  pd.read_csv(os.path.join(os.path.abspath("."), "data", "warmline", file)).dropna(axis="columns", how="all").dropna(axis="index") for file in list(os.walk("data/warmline"))[0][2]])

df["Date"] = df["Date"].apply(pd.to_datetime)
df["YOB"] = df["YOB"].astype(str).replace(" ", "").replace("", 0)
df["Age"] = 2024 - df["YOB"].astype(float).astype(int)
#df["Date"] = df["Date"].apply(lambda x: 2000)
df["Count"] = np.ones(len(df["Date"]))
df = df[["Date", "Count"]]



# plot
fig, ax = plt.subplots(figsize=(6, 4))
#colors = {'female': 'Pink', 'male': 'Navy'}
#for kind, data in df.groupby('Gender'):
#    data.plot(kind='scatter', x='Date', y='Age', label=kind, color=colors[kind], ax=ax, figsize=(8, 4))

ax.set(xlabel='Month')


df = df.set_index("Date")
#print(df.reindex(index=df["Date"]).resample('MS').sum())
print(df.resample('MS').sum().plot())


#print(pd.to_datetime("1/3/2020") in pd.date_range("1/1/2020", "2/1/2022", freq="D"))
#dates = pd.date_range(start=df["Date"].min(), end=df["Date"].max(), freq="ME")





ax.tick_params(reset=True, direction='out', pad=1.0, width=1, labelsize="small",zorder=2)
fig.suptitle('Avg Use / Month')
 # NOTE This graph isn't very helpful
plt.savefig("images/totalcountsovertime.png")