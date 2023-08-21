import tkinter as tk
from tkinter import ttk


window = tk.Tk()
window.title('Pack & Frames')
window.geometry('800x500+350+170')

# top frame
top_frame = ttk.Frame(window)
label1 = ttk.Label(top_frame, text='First Label', background='red')
label2 = ttk.Label(top_frame, text='Label 2', background='blue')

# middle widgets
label3 = ttk.Label(window, text='Another Label', background='green')


# bottom frame
bottom_frame = ttk.Frame(window)
label4 = ttk.Label(bottom_frame, text='Last Label', background='orange')
button1 = ttk.Button(bottom_frame, text='A Button')
button2 = ttk.Button(bottom_frame, text='Another Button')


# top layout
top_frame.pack(fill='both', expand=True)
label1.pack(side='left', fill='both', expand=True)
label2.pack(side='left', fill='both', expand=True)

# middle layout
label3.pack(expand=True)

# bottom layout
bottom_frame.pack(expand=True, fill='both', padx=20, pady=20)
button1.pack(side='left', expand=True, fill='both')
label4.pack(side='left', expand=True, fill='both')
button2.pack(side='left', expand=True, fill='both')

# exercise
ex_frame = ttk.Frame(bottom_frame)
button3 = ttk.Button(ex_frame, text='Button 3')
button4 = ttk.Button(ex_frame, text='Button 4')
button5 = ttk.Button(ex_frame, text='Button 5')

ex_frame.pack(side='left', expand=True, fill='both')
button3.pack(expand=True, fill='both')
button4.pack(expand=True, fill='both')
button5.pack(expand=True, fill='both')


window.bind('<Escape>', lambda event: window.quit())
window.mainloop()














