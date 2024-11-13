import pandas as pd
import os
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

import matplotlib.cbook as cbook
import matplotlib.dates as mdates


from head import df


df = df[["Age", "Date", "Gender"]]

df = df[df["Age"] < 100 ]


# plot
fig, ax = plt.subplots(figsize=(6, 4))
colors = {'female': 'Pink', 'male': 'Navy'}
for kind, data in df.groupby('Gender'):
    data.plot(kind='scatter', x='Date', y='Age', label=kind, color=colors[kind.strip()], ax=ax, figsize=(8, 4))

ax.set(xlabel='Date', ylabel='Age')


labels = ax.get_xticklabels()
plt.setp(labels, rotation=85, fontsize=8)



#dates = pd.date_range(start=df["Date"].min(), end=df["Date"].max(), freq="ME")




print(df["Date"].min())
# Format x-axis labels as months
ax.xaxis.set_major_locator(mdates.MonthLocator())
ax.xaxis.set_major_formatter(mdates.DateFormatter('%b'))

# Rotate x-axis labels if needed
plt.xticks(rotation=45)



ax.tick_params(reset=True, direction='out', pad=1.0, width=1, labelsize="small",zorder=2)

fig.suptitle('Male vs Female')

from func import save
save(__file__)