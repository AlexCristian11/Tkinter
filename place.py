import tkinter as tk
from tkinter import ttk


window = tk.Tk()
window.title('Place')
window.geometry('500x400+950+200')

# widgets
label1 = ttk.Label(window, text='Label 1', background='red')
label2 = ttk.Label(window, text='Label 2', background='blue')
label3 = ttk.Label(window, text='Label 3', background='green')
button1 = ttk.Button(window, text='Button 1')


# layout
label1.place(x=100, y=200, width=300, height=50)
label2.place(relx=0.2, rely=0.3, relwidth=.4, relheight=.5)
label3.place(x=100, y=120, width=200, height=200)
button1.place(relx=1, rely=1, anchor='se')

# frame
frame = ttk.Frame(window)
frame_label = ttk.Label(frame, text='Frame Label', background='yellow')
frame_button = ttk.Button(frame, text='Frame Button')


# frame layout
frame.place(relx=0, rely=0, relwidth=.3, relheight=1)
frame_label.place(relx=0, rely=0, relwidth=1, relheight=.5)
frame_button.place(relx=0, rely=.5, relwidth=1, relheight=.5)

# exercise
label4 = ttk.Label(window, text='Label Exercise', background='orange')
label4.place(relx=.5, rely=.5, relwidth=.5, relheight=.5, anchor='center')

# run
window.bind('<Escape>', lambda event: window.quit())
window.mainloop()
