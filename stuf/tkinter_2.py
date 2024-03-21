import tkinter as tk
c = tk.Tk()
c.title('jauns window') # loga vārds
c.geometry("600x400") # loga lielums
message = tk.Label(c, text="ievadi savu vārdu")
message.pack()

l = tk.Entry(c)
l.pack()

def click():
    message.configure(text = 'sveiki' + l.get())
pog = tk.Button(c, text='Submit', command = click)
pog.pack()


c.mainloop()