import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data-firearm.csv")
df.fillna(0, inplace = True)
labels = ["handgun", "long_gun", "others"]
others = []
p = [sum(df.loc[:, "handgun"]), sum(df.loc[:, "long_gun"])]
mycolors = ['#1f77b4', '#ff7f0e', '#2ca02c']
for column in df :
    if column != "month" and column != "state" and column != "totals" and column != "handgun" and column != "long_gun" :
        others.append(sum(df.loc[:, column]))
p.append(sum(others))

plt.pie(p, labels = labels, colors = mycolors, autopct='%1.1f%%')
plt.show()