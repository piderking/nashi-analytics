import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

DATA_DIRECTOR = "data/"

df = pd.read_csv(DATA_DIRECTOR+"08-24.csv")


# Assume 'year_of_birth' column exists in the DataFrame
df['age'] = 2024 - df['YOB']

# Create age group categories
bins = [0, 18, 25, 35, 45, 60, 100]
labels = ['Under 18', '18-25', '26-35', '36-45', '46-60', '60+']
df['age_group'] = pd.cut(df['age'], bins=bins, labels=labels)

# Stratify by age group
age_group_counts = df['age_group'].value_counts()
print(age_group_counts.head())

df['age_group'].hist()


"""

plt.plot(x, y, color='green', linestyle='dashed', linewidth = 3,
         marker='o', markerfacecolor='blue', markersize=12)

# setting x and y axis range


# naming the x axis
plt.xlabel('Date')
# naming the y axis
plt.ylabel('Year of Birth')

# giving a title to my graph
plt.title('Graph')

"""
"""
# setting the ranges and no. of intervals
range = (0, 100)
bins = 10  

# plotting a histogram
plt.hist(data["Zip"], bins, range, color = 'green',
        histtype = 'bar', rwidth = 0.8)

# x-axis label
plt.xlabel('age')
# frequency label
plt.ylabel('No. of people')
# plot title
plt.title('My histogram')
"""
# function to show the plot
plt.savefig("images/plt.png")