import pandas as pd
data = {
    "calories" : [420,380,390],
    "duration" : [50,40,45]
}
df = pd.DataFrame(data)
df
data = {
    "calories" : [420,380,390],
    "duration" : [50,40,45]
}
df = pd.DataFrame(data)
print(df)
data = {
    "calories" : [420,380,390],
    "duration" : [50,40,45]
}
df = pd.DataFrame(data)
df.loc[0]
data = {
    "calories" : [420,380,390],
    "duration" : [50,40,45]
}
df = pd.DataFrame(data)
df["calories"].loc[0]
data = {
    "Characters" : ["A","B","C"],
    "Number" : [32,50,2]
}
df = pd.DataFrame(data)
data = {
    "Characters" : ["A","B","C"],
    "Number" : [32,50,2]
}
df = pd.DataFrame(data)
df.loc[1]
data = {
    "Characters" : ["A","B","C"],
    "Number" : [32,50,2]
}
df = pd.DataFrame(data)
df.loc[2][1]
data = {
    "Characters" : ["A","B","C"],
    "Number" : [32,50,2]
}
df = pd.DataFrame(data)
df["Number"][2]