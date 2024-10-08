import pandas as pd
import os
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

#files = pd.read_csv("data/01-24.csv")
pd.DataFrame()

from head import df

df["Date"] = df["Date"].apply(pd.to_datetime)
df["YOB"] = df["YOB"].astype(str).replace(" ", "").replace("", 0)
df["Age"] = 2024 - df["YOB"].astype(float).astype(int)
#df["Date"] = df["Date"].apply(lambda x: 2000)
df["Count"] = np.ones(len(df["Date"]))
df = df[["Date", "Count", "Gender"]]



# plot
fig, ax = plt.subplots(figsize=(6, 4))
colors = {'female': 'Pink', 'male': 'Navy'}

df = df.set_index("Date")

for kind, data in df.groupby('Gender'):
    data.resample("MS").sum().plot(label=str(kind), color=colors[kind.strip()], ax=ax, legend=str(kind))

ax.set(xlabel='Month', ylabel="Times Used")

#df = df.set_index("Date")
#print(df.reindex(index=df["Date"]).resample('MS').sum())
#print(df.resample('MS').sum().plot())


#print(pd.to_datetime("1/3/2020") in pd.date_range("1/1/2020", "2/1/2022", freq="D"))
#dates = pd.date_range(start=df["Date"].min(), end=df["Date"].max(), freq="ME")




ax.legend(["Female", "Male"]);

ax.tick_params(reset=True, direction='out', pad=1.0, width=1, labelsize="small",zorder=2)
fig.suptitle('Male v. Female Monthly Usage')
 # NOTE This graph isn't very helpful
from func import save
save(__file__)