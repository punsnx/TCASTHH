df = pd.read_csv("data.csv")
x=0
for i in df["Duration"] :
  x += i
print(x)
for i in df.index :
  if df.loc[i, "Maxpulse"] > 120 :
    df.loc[i, "Maxpulse"] = 120
    
df
df.dropna(inplace = True)
for i in df.index :
  if df.loc[i, "Calories"] <= 400 :
    df.drop(i, inplace = True)
df
df = pd.read_csv("data.csv")

df.dropna(inplace = True)
for i in df.index :
  if df.loc[i, "Duration"] <= df.loc[i, "Pulse"] :
    df.drop(i, inplace=True)

df
df.fillna(0, inplace = True)
df = df[df["Duration"] > df["Pulse"]]
df