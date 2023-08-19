import tkinter as tk
from tkinter import ttk


window = tk.Tk()
window.title('Frames')
window.geometry('800x500')


# frame
frame = ttk.Frame(window, width=200, height=200, borderwidth=1, relief=tk.GROOVE)
frame.pack_propagate(False)
frame.pack(side='left')

# master setting

label = ttk.Label(frame, text='Label in frame')
label.pack()

button = ttk.Button(frame, text='button is in frame')
button.pack()

label2 = ttk.Label(window, text='Label outside the frame')
label2.pack()

#
frame2 = ttk.Frame(window, width=200, height=200, borderwidth=5, relief=tk.GROOVE)
frame2.pack_propagate(False)
frame2.pack(side='right')

label3 = ttk.Label(frame2, text='Exercise label')
label3.pack()

button2 = ttk.Button(frame2, text='Exercise button')
button2.pack()


window.mainloop()
