import pandas as pd
import numpy

import statistics
df = pd.read_csv("foodkakkak.csv")
df.dropna(inplace = True)
l = []
for i in df.index :
    l.append(int(str(df.loc[i, "Kind"])[0:1]))

print(statistics.mode(l))