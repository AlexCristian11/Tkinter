import tkinter as tk
from tkinter import ttk


window = tk.Tk()
window.title('Tabs')
window.geometry('800x500')

# notebook widget
notebook = ttk.Notebook(window)

# tab 1
tab1 = ttk.Frame(notebook)
label1 = ttk.Label(tab1, text='Text in tab 1')
label1.pack()
button1 = ttk.Button(tab1, text='button in tab 1')
button1.pack()


# tab 2
tab2 = ttk.Frame(notebook)
label2 = ttk.Label(tab2, text='label in tab 1')
label2.pack()
entry2 = ttk.Entry(tab2)
entry2.pack()


# tab 3
tab3 = ttk.Frame(notebook)
button3 = ttk.Button(tab3, text='Button in tab 3')
button3.pack()

button4 = ttk.Button(tab3, text='Button in tab 3')
button4.pack()

label3 = ttk.Label(tab3, text='Text in tab 3')
label3.pack()


notebook.add(tab1, text='Tab 1')
notebook.add(tab2, text='Tab 2')
notebook.add(tab3, text='Tab 3')
notebook.pack()


window.mainloop()