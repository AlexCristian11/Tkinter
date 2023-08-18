import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.title('ComboBox and SpinBox')
window.geometry('800x500')

# combobox
items = ('Ice Cream', 'Pizza')
food_string = tk.StringVar(value=items[0])
combo = ttk.Combobox(window, textvariable=food_string)
combo['values'] = items
# combo.config(values=items)
combo.pack()

# event
combo.bind('<<ComboboxSelected>>', lambda event: combo_label.config(text=f"Selected value: {food_string.get()}", pady=20))

combo_label = tk.Label(window, text='label', pady=20)
combo_label.pack()


# spinbox
spin_int = tk.IntVar(value=12)
spin = ttk.Spinbox(window,
                   from_=1, to=20,
                   increment=3,
                   command=lambda : print(spin_int.get()),
                   textvariable=spin_int)
spin.bind('<<Increment>>', lambda event: print('up'))
spin.bind('<<Decrement>>', lambda event: print('down'))
spin.pack()


spin_ex = ttk.Spinbox(window)
spin_ex['value'] = ('A', 'B', 'C', 'D', 'E')
spin_ex.pack()
spin_ex.bind('<<Decrement>>', lambda event: print(spin_ex.get()))

window.mainloop()
