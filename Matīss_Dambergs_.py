import tkinter as tk
from tkinter import ttk
import math

from tkinter import *  
from tkinter import messagebox  

c = tk.Tk() #definet galveno logu
c.title('fizikas formulu aprēķins') # loga vārds
c.geometry("600x400") # loga lielums
c.iconbitmap('skoladarbins/electron_94377.ico') # ievieto logo pie loga 
k = tk.Label(c, text="Fizikas formula elektribas stiprumam ")
k.pack()

c = Tk()  
c.geometry("100x100")


k1= tk.Label(c, text = 'ievadi  spriegumu, pretestību')
k1.pack()

k2 = tk.Label(c,text = 'ievadi pretestību ')
k2.pack()

e = tk.Entry(c)
e.place(x=-60, y=60)

e1 = tk.Entry(c)
e1.place(x= -60, y = 20)
 
def izrēķināt():
    try:
        results = float(e.get() / float(e1.get()))
        c.configure(text = results)

    except:ValueError
    messagebox.showerror('vai esi pārliecināts')

pog = tk.Button(c, text = 'veikt aprēķinus', command = izrēķināt, )
  




c.mainloop()