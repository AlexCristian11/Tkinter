import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.title('Tkinter Variables')
window.geometry('800x500')


def button_func():
    print(string_var.get())
    string_var.set('button pressed')


# tkinter variables
string_var = tk.StringVar(value='start value')


label = ttk.Label(master=window, text='Label', textvariable=string_var)
label.pack()

entry = ttk.Entry(master=window, textvariable=string_var)
entry.pack()

button = ttk.Button(master=window, text='Button', command=button_func)
button.pack()

string_var1 = tk.StringVar(value='test')

label1 = ttk.Label(master=window, text='Label', textvariable=string_var1)
label1.pack()

ex_entry1 = ttk.Entry(master=window, textvariable=string_var1)
ex_entry1.pack()

ex_entry2 = ttk.Entry(master=window, textvariable=string_var1)
ex_entry2.pack()


window.mainloop()
