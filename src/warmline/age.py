import pandas as pd
import os
import matplotlib.pyplot as plt
import numpy as np


from head import df

d = df[df["Age"] < 100 ]


plot = d[["Age", "Gender"]].groupby("Gender").boxplot( patch_artist=True, return_type='dict')

from func import save
save(__file__)