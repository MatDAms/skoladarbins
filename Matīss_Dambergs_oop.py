import tkinter as tk
from tkinter import ttk
import math
c = tk.Tk() #definet galveno logu
c.title('fizikas formulu aprēķins') # loga vārds
c.geometry("600x400") # loga lielums
c.iconbitmap('skoladarbins/electron_94377.ico') # ievieto logo pie loga 
message = tk.Label(c, text="Fizikas")
message.pack()

e = tk.Entry(c)
e.place(x=-60, y=60)

e1 = tk.Entry(c)
e1.place(x= -60, y = 20)







c.mainloop()