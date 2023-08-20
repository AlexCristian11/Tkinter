import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.title('Layout Intro')
window.geometry('800x500+370+150')
window.resizable(True, True)

# widgets
label1 = ttk.Label(window, text='Label 1', background='red')
label2 = ttk.Label(window, text='Label 2',background='green')

# pack
# label1.pack(side='left', expand=True, fill='both')
# label2.pack(side='right', expand=True, fill='both')

# grid
# window.columnconfigure(0, weight=1)
# window.columnconfigure(1, weight=1)
# window.columnconfigure(2, weight=2)
# window.rowconfigure(0, weight=1)
# window.rowconfigure(1, weight=1)
#
# label1.grid(row=0, column=1, sticky='nsew')
# label2.grid(row=1, column=1, columnspan=2, sticky='nsew')


# place
label1.place(x=200, y=100, width=200, height=200)
label2.place(relx=0.5, rely=0.5, relwidth=1, anchor='se')



window.bind('<Escape>', lambda event: window.quit())
window.mainloop()
