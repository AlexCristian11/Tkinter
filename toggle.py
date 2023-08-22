import tkinter as tk
from tkinter import ttk


window = tk.Tk()
window.title('Toggle widgets')
window.geometry('500x400+950+200')

# place
# def toggle_label():
#     global label_toggle
#
#     if label_toggle:
#         label.place_forget()
#         label_toggle = False
#     else:
#         label_toggle = True
#         label.place(relx=.5, rely=.5, anchor='center')
#
#
# button = ttk.Button(window, text='Toggle label', command=toggle_label)
# button.place(x=10, y=10)
#
# label_toggle = True
# label = ttk.Label(window, text='Label')
# label.place(relx=.5, rely=.5, anchor='center')

# grid
# def toggle_label():
#     global label_toggle
#
#     if label_toggle:
#         label.grid_forget()
#         label_toggle = False
#     else:
#         label_toggle = True
#         label.grid(column=1, row=0)
#
#
# window.columnconfigure((0,1), weight=1, uniform='a')
# window.columnconfigure(0, weight=1, uniform='a')
#
# button = ttk.Button(window, text='Toggle label',command=toggle_label)
# button.grid(column=0, row=0)
#
# label_toggle = True
# label = ttk.Label(window, text='Label')
# label.grid(column=1, row=0)

# pack
def toggle_label():
    global label_toggle
    if label_toggle:
        label.pack_forget()
        label_toggle = False
        frame.pack(expand=True, before=button)
    else:
        frame.pack_forget()
        label.pack(expand=True, before=button)
        label_toggle = True


label_toggle = True
label = ttk.Label(window, text='Label')
label.pack(expand=True)
button = ttk.Button(window, text='Toggle label')
button.pack()
button = ttk.Button(window, text='Toggle label', command=toggle_label)
button.pack()

frame = ttk.Frame(window)



# run
window.bind('<Escape>', window.quit())
window.mainloop()
