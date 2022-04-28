import tkinter as tk
from tkinter import ttk
app = tk.Tk()
app.title("Sirisuk")
app.geometry('350x200')
total = 0
def pl() :
    total = int(ent1.get()) + int(ent2.get())
    Label.configure(text=total)
def mi() :
    total = int(ent1.get()) - int(ent2.get())
    Label.configure(text=total)
def mu() :
    total = int(ent1.get()) *+ int(ent2.get())
    Label.configure(text=total)
def de() :
    total = int(ent1.get()) / int(ent2.get())
    Label.configure(text=total)
ent1 = tk.Entry(app, width=20)
ent2 = tk.Entry(app, width=20)
plus = tk.Button(text='+', command=pl)
minus = tk.Button(text='-', command=mi)
multiply = tk.Button(text='*', command=mu)
devide = tk.Button(text='/', command=de)

Label = tk.Label(text='X')



plus.grid(column=2, row=0)
minus.grid(column=3, row=0)
multiply.grid(column=4, row=0)
devide.grid(column=5, row=0)
ent1.grid(column=0, row=0)
ent2.grid(column=1, row=0)
Label.grid(column=0,row=2)
app.mainloop()