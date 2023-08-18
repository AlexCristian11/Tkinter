import tkinter as tk
from tkinter import ttk


def button_func():
    print('a button')


def button_hello():
    print("Hello")


# create a window
window = tk.Tk()
window.title('Window and Widgets')
window.geometry('800x550')

# ttk widgets

label = ttk.Label(master=window, text='This is a test')
label.pack()


# tk.text

text = tk.Text(master=window)
text.pack()


label_td = ttk.Label(master=window, text='My label')
label_td.pack()
button_td = ttk.Button(master=window, text='Hello', command=lambda: print('hello'))
button_td.pack()


# ttk entry

entry = ttk.Entry(master=window)
entry.pack()

# ttk button
button = ttk.Button(master=window, text='A button', command=button_func)
button.pack()


# run
window.mainloop()