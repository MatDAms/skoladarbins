import tkinter as tk
from tkinter import ttk


root = tk.Tk()
root.title('Mana pirmā programma!!!')
root.geometry('600x400+100+100')
root.resizable(False, False)
# root.attributes('-alpha', 0.5)
root.iconbitmap('skoladarbins/electron_94377.ico')
# place a label on the root window
message = tk.Label(root, text="Sveika pasaule!")
message.pack()
ttk.Label(root, text='Themed Label').pack()

def button_clicked():
    print('Button clicked')


button = ttk.Button(root, text='Click Me', command=button_clicked)

button.pack()

def select(option):
    print(option)


ttk.Button(root, text='Rock', command=lambda: print('Rock')).place(x = 450,y = 50)
ttk.Button(root, text='Paper',command=lambda: print('Paper')).place(x = 450, y = 90)
ttk.Button(root, text='Scissors', command=lambda: print('Scissors')).place(x= 450, y = 130)
# keep the window displaying
Username = ttk.Label(root, text = "Username").place(x = 10,y = 50)  
email = ttk.Label(root, text = "Email").place(x = 10, y = 90)  
password = ttk.Label(root, text = "Password").place(x = 10, y = 130)
e1 = ttk.Entry(root).place(x = 80, y = 50)  
e2 = ttk.Entry(root).place(x = 80, y = 90)  
e3 = ttk.Entry(root).place(x = 95, y = 130)  
ttk.Button(root, text='Submit', command=lambda: print('Submit')).place(x= 10, y = 170)

photo = tk.PhotoImage(file='skoladarbins/valentines-day.png')
image_label = ttk.Label(root,image=photo,padding=5)
image_label.pack()
root.mainloop()