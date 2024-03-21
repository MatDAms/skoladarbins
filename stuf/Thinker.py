import tkinter as tk
from tkinter import ttk
c = tk.Tk() #definet galveno logu
c.title('jauns window') # loga vārds
c.geometry("600x400") # loga lielums
message = tk.Label(c, text="programmējam")
message.pack()
def clicked():
    message.configure(text = "ko dari!!!")



button = ttk.Button(c, text='Nospied mani',command = clicked) # ievieto pogu
button.pack()

def click():
    message.configure(text ="")
but = tk.Button(c, text= "delete", fg = "red", command = click)
but.pack()

c.mainloop() # programmas palaišana