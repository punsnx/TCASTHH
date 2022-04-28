import random 
import sys
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import tkinter as tk

wf = tk.Tk()
wf.title("Weather Food Recommandation")
wf.geometry('1280x720')
df = pd.read_csv("Weather_Food.csv")
for i in df.index :
    labels = df.loc[i, "Name_TH"] + " " + str(df.loc[i, "RATE"])
    label = tk.Label(text=labels)
    label.grid(column=0,row=i)
wf.mainloop()