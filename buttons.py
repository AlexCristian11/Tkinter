import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.title('Buttons')
window.geometry('800x500')


# button

def button_func():
    print('a simple button')
    print(radio_var.get())


button_string = tk.StringVar(value='A button with StringVar')
button = ttk.Button(master=window, text='A simple button', command=button_func, textvariable=button_string)
button.pack()

# a check button
check_var = tk.IntVar()
checkbox1 = ttk.Checkbutton(master=window, text='CheckBox1', command=lambda: print(check_var.get()), variable=check_var)
checkbox1.pack()

# radio buttons
radio_var = tk.StringVar()
radio1 = tk.Radiobutton(window, text='Radiobutton 1', value='radio 1', variable=radio_var,
                        command=lambda : print(radio_var.get()))
radio1.pack()
radio2 = tk.Radiobutton(window, text='Radiobutton 2', value='radio 2', variable=radio_var,
                        command=lambda : print(radio_var.get()))
radio2.pack()


#

def radio_func():
    print(ex_check_var.get())
    ex_check_var.set(False)


ex_check_var = tk.BooleanVar()
ex_checkbutton = tk.Checkbutton(window, text='Ex Checkbox', variable=ex_check_var, command=lambda : print(ex_radio_var.get()))
ex_checkbutton.pack()

ex_radio_var = tk.StringVar()
ex_radio1 = tk.Radiobutton(window, text='Ex Radiobutton 1', value='ex radio 1', variable=ex_radio_var,
                           command=radio_func)
ex_radio1.pack()

ex_radio2 = tk.Radiobutton(window, text='Ex Radiobutton 2', value='ex radio 2', variable=ex_radio_var,
                           command=radio_func)
ex_radio2.pack()

window.mainloop()
