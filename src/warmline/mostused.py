import pandas as pd
import os
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns



from head import df

df["Date"] = df["Date"].apply(pd.to_datetime)
df["YOB"] = df["YOB"].astype(str).replace(" ", "").replace("", 0)
df["Age"] = 2024 - df["YOB"].astype(float).astype(int)
#df["Date"] = df["Date"].apply(lambda x: 2000)
df = df[["Age", "Date", "Gender"]]


# plot
fig, ax = plt.subplots(figsize=(6, 4))
colors = {'female': 'Pink', 'male': 'Navy'}
for kind, data in df.groupby('Gender'):
    data.plot(kind='scatter', x='Date', y='Age', label=kind, color=colors[kind.strip()], ax=ax, figsize=(8, 4))

ax.set(xlabel='Date', ylabel='Age')







#dates = pd.date_range(start=df["Date"].min(), end=df["Date"].max(), freq="ME")

label  = pd.date_range(df["Date"].min(), df["Date"].max(), freq="MS")




ax.tick_params(reset=True, direction='out', pad=1.0, width=1, labelsize="small",zorder=2)
fig.suptitle('Male vs Female')


from func import save
save(__file__)