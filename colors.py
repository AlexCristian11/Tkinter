import tkinter as tk
from tkinter import ttk


window = tk.Tk()
window.title('Colors')
window.geometry('900x600+350+100')

# widgets
ttk.Label(window, background='#5A6').pack(expand=True, fill='both')
ttk.Label(window, background='#D22').pack(expand=True, fill='both')
ttk.Label(window, background='#08F').pack(expand=True, fill='both')

# exercise
ttk.Label(window, background='#422').pack(expand=True, fill='both')

# run
window.mainloop()
