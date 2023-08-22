import tkinter as tk
from tkinter import ttk


window = tk.Tk()
window.title('Stacking')
window.geometry('500x400+950+200')


# widgets
label1 = ttk.Label(window, text='Label 1', background='orange')
label2 = ttk.Label(window, text='Label 2', background='red')
label3 = ttk.Label(window, text='Label 3', background='yellow')
# label2.lower()


button1 = ttk.Button(window, text='raise label 1', command=lambda: label1.tkraise(aboveThis= label2))
button2 = ttk.Button(window, text='raise label 2', command=lambda: label2.lift())
button3 = ttk.Button(window, text='raise label 3', command=lambda: label3.lift())
# layout
label1.place(x=50, y=100, width=200, height=150)
label2.place(x=150, y=60, width=140, height=100)
label3.place(x=100, y=150, width=300, height=50)

button1.place(rely=1, relx=.6, anchor='se')
button2.place(rely=1, relx=.8, anchor='se')
button3.place(rely=1, relx=1, anchor='se')


# run
window.bind('<Escape>', lambda event: window.quit())
window.mainloop()