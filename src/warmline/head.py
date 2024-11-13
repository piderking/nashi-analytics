import pandas as pd
import os


#lis = zip([  pd.read_csv(os.path.join(os.path.abspath("."), "data", "warmline", file), index_col=False) for file in list(os.walk("data/warmline"))[0][2]],  list(os.walk("data/warmline"))[0][2])




d = pd.concat( [  pd.read_csv(os.path.join(os.path.abspath("."), "data", "warmline", file)) for file in list(os.walk("data/warmline"))[0][2]])



d["Date"] = pd.to_datetime(d["Date"])


d["Gender"] = d["Gender"].str.strip()
d["City"] = d["City"].str.strip()


d["Age"] = 2024 - d["Year of Birth"].astype(str).replace(" ", "").replace("", 0).astype(float).astype(int)



"""
If Age Matters: 

d = df[df["Age"] < 100 ]


"""

print(d["Date"].min())
#print(d["Age"].value_counts())

# TODO Add Age
df = d


