import tkinter as tk
from tkinter import ttk


window = tk.Tk()
window.title('Menu')
window.geometry('800x500')


menu = tk.Menu(window)

# sub menu
file_menu = tk.Menu(menu, tearoff=False)
file_menu.add_command(label='New', command=lambda : print('new file'))
file_menu.add_command(label='Open', command=lambda : print('open file'))
file_menu.add_separator()
menu.add_cascade(label='File', menu=file_menu)


# another sub menu
help_menu = tk.Menu(menu, tearoff=False)
help_menu.add_command(label='Help Entry', command=lambda: print(help_check_string.get()))
help_check_string = tk.StringVar()
help_menu.add_checkbutton(label='Check', onvalue='on', offvalue='off', variable=help_check_string)
menu.add_cascade(label='Help', menu=help_menu)

# menu button
menu_button = ttk.Menubutton(window, text='Menu Button')
menu_button.pack()

button_submenu = tk.Menu(menu_button, tearoff=False)
button_submenu.add_command(label='entry 1', command=lambda : print('entry 1'))
button_submenu.add_checkbutton(label='check 1')
menu_button.configure(menu=button_submenu)


#
ex_menu = tk.Menu(menu, tearoff=False)
ex_menu.add_command(label='exercise test 1')
menu.add_cascade(label='Exercise', menu=ex_menu)

ex_submenu = tk.Menu(menu, tearoff=False)
ex_submenu.add_command(label='some more stuff')
ex_menu.add_cascade(label='more stuff', menu=ex_submenu)


window.configure(menu=menu)


window.mainloop()
