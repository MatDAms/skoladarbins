import math
import tkinter as tk
from tkinter import ttk
# c = tk.Tk() #definet galveno logu
# c.title('jauns window') # loga vārds
# c.geometry("600x400") # loga lielums
# message = tk.Label(c, text="Uzdevums")
# message.pack()

# e= tk.Entry(c)
# e.place(x =200, y=60)

# e1 = tk.Entry(c)
# e1.place(x=200,y=100)

# def click():
#     message.configure(text = int(e.get()) + "" + int(e1.get()))
# pog = tk.Button(c, text='Submit', command = click)
# pog.pack()

# photo = tk.PhotoImage(file='skoladarbins/valentines-day.png')
# image_label = ttk.Label(c,image=photo,padding=5)
# image_label.pack(pady =120)
# def funky():
#     try:
#         message.configure(text = int(e.get()) + "" + int(e1.get()))
#     except: ValueError
#     message = tk.Label(c, text="nevar šādu atbildi iegūt")

# c.mainloop()

c = tk.Tk() #definet galveno logu
c.title('jauns window') # loga vārds
c.geometry("600x400") # loga lielums
message = tk.Label(c, text="ievadi slaitli")
message.pack()

pog = tk.Button(c, text='Submit',)
pog.pack

e = tk.Entry(c)
e.palce(x = 100, y = 150)

def click ():
    try:
        message.configure(text = 'izskāpinats', math.sqrt(int(e.get())))
    except: ValueError
    