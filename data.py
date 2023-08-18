import tkinter as tk
from tkinter import ttk


def button_func():
    entry_text = entry.get()
    # update the label
    # label.config(text='some other text')
    label['text'] = entry_text
    entry['state'] = 'disabled'


window = tk.Tk()
window.title('Getting and setting widgets')
window.geometry('800x500')

label = ttk.Label(master=window, text='Label')
label.pack()

entry = ttk.Entry(master=window)
entry.pack()

button = ttk.Button(master=window, text='A button', command=button_func)
button.pack()

def change():
    label['text'] = 'some text'
    entry['state'] = 'enabled'


ex_button = ttk.Button(master=window, text='Change', command=change)
ex_button.pack()


window.mainloop()
