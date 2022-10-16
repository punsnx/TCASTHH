import pandas as pd
df = pd.read_csv("Medals.csv")
print("Gold : " + str(df.loc[:, "Gold"].sum()))
print("Silver : " + str(df.loc[:, "Silver"].sum()))
print("Bronze : " + str(df.loc[:, "Bronze"].sum()))
x = df.loc[:, "Gold"].sum() + df.loc[:, "Silver"].sum() + df.loc[:, "Bronze"].sum()
print(x)
for i in df.index :
  print(df["Team/NOC"].loc[i] + " : " + str(df.loc[i, "Gold"] + df.loc[i, "Silver"] + df.loc[i, "Bronze"]))
  sum = []
for i in df.index :
  sum.append(df.loc[i, "Gold"] + df.loc[i, "Silver"] + df.loc[i, "Bronze"])

df.insert(5, "SUM", sum)
df
df.drop_duplicates(subset = "Gold", keep = False, inplace = True)

print(df.to_string())