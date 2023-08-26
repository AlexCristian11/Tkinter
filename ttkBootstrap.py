import tkinter as tk
from tkinter import ttk
import ttkbootstrap as ttk


window = ttk.Window(themename='darkly')
window.title('Ttkbootstrap')
window.geometry('800x600+400+100')

# widgets
label = ttk.Label(window, text='Label')
label.pack()

button1 = ttk.Button(window, text='Button 1', bootstyle='danger-outline')
button1.pack(pady=10)

button2 = ttk.Button(window, text='Button 2', bootstyle='warning-outline')
button2.pack(pady=10)

button3 = ttk.Button(window, text='Button 3', bootstyle='success-outline')
button3.pack(pady=10)


# run
window.mainloop()
