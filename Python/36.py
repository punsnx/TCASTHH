import random 
import sys
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv("Medals.csv")
x = []
y = []
mycolors = []
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd','#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf']
for i in range(10) :
    x.append(df.loc[i, "Team/NOC"])
    y.append(df.loc[i, "Gold"] + df.loc[i, "Silver"] + df.loc[i, "Bronze"])
    mycolors.append(random.choice(colors))

plt.figure(figsize=(30, 10))
plt.bar(x, y, color = mycolors)
plt.grid()
plt.show()