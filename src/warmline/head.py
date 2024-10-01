import pandas as pd
import os

d = pd.concat( [  pd.read_csv(os.path.join(os.path.abspath("."), "data", "warmline", file), index_col=False).dropna(axis="columns", how="all").dropna(axis="index") for file in list(os.walk("data/warmline"))[0][2]])


# Modifications to data set

d["Gender"] = d["Gender"].str.strip()

df = d


