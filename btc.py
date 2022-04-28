import pandas as pd

df = pd.read_csv("skpc-2022-04-27.csv")

total = []
for i in df.index :
    total.append(df.loc[i, "unpaid_total_amount"])


print(sum(total))