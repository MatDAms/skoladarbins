import tkinter as tk
from tkinter import ttk
import math

from tkinter import *  
from tkinter import messagebox  

c = tk.Tk() #definet galveno logu
c.title('fizikas formulu aprēķins') # loga vārds
c.geometry("600x400") # loga lielums
c.iconbitmap('skoladarbins/electron_94377.ico') # ievieto logo pie loga 
k = tk.Label(c, text="Fizikas formula elektribas spriegumma ")
k.pack()

k3 = tk.Label(c,text = 'nav nekads rezultats') # izveido nosaukuma loga
k3.place(x = 120, y= 140)

k1= tk.Label(c, text = 'ievadi pretestību')# izveido nausaukumu logā
k1.pack()

k2 = tk.Label(c,text = 'ievadi stiprumu ') # izveidoju nosaukumu loga
k2.place(x = 200, y=60 )

e = tk.Entry(c)
e.place(x=60, y=60)# ievieto vietu kur var ierkastit skaitļus

e1 = tk.Entry(c) # ievieto kur var ievadit skaitļus
e1.place(x= 60, y = 20)
 
def izrēķināt():
    try:
        results = float(e.get() * e1.get()) # no vadīšanas vietas sareizina abus ievietotos
        k3.configure(text = 'Rezultāts' + int(results))

    except:ValueError
    messagebox.showerror('nepareizi') # nav pareizi sakitļi ievietoti, kļūda rada

pog = tk.Button(c, text = 'veikt aprēķinus', command = izrēķināt, background= 'red' ) # poga ar kuru veic sareizināšanu un mainita ta krasa
pog.place(x= 80, y= 100 )
  
photo = tk.PhotoImage(file='skoladarbins/valentines-day.png') # ievietotā bilde
image_label = ttk.Label(c,image=photo,padding=5)
image_label.place(x =200 , y =225 )



c.mainloop() # programmas beigas