import tkinter as tk
from tkinter import ttk


window = tk.Tk()
window.title('Pack')
window.geometry('800x500+350+150')


# widgets
label1 = ttk.Label(window, text='Label 1', background='red')
label2 = ttk.Label(window, text='Label 2', background='blue')
label3 = ttk.Label(window, text='Label 3', background='green')
button = ttk.Button(window, text='Button')


# layout
label1.pack(side='left', expand=True, fill='both')
label2.pack(side='top', expand=True, fill='both')
label3.pack(side='top', expand=True, fill='both')
button.pack(side='top', expand=True, fill='both')


window.bind('<Escape>', lambda event: window.quit())
window.mainloop()
