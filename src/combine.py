import pandas as pd
import os
import matplotlib.pyplot as plt

files = pd.read_csv("data/warmline-header.csv")


df = pd.concat( [  pd.read_csv(os.path.join(os.path.abspath("."), "data", "warmline", file)) for file in list(os.walk("data/warmline"))[0][2]])
#df['age'] = 2024 - df['YOB']
