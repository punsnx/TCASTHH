import pandas as pd
import matplotlib.pyplot as plt
import random

df = pd.read_csv("data-firearm.csv")
df.fillna(0, inplace = True)
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd','#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf']
mycolors = []
labels = []
totals  = [] 
for i in df.index :
    if df.loc[i, "month"] == "2021-06" :
        labels.append(df.loc[i, "state"])
        totals.append(df.loc[i, "totals"])
        mycolors.append(random.choice(colors))
plt.figure(figsize=(10, 30))
plt.grid()
plt.barh(labels, totals, color = mycolors)
plt.show()