import tkinter as tk
from tkinter import ttk


def get_pos(event):
    print(f"x: {event.x} y:{event.y}")


window = tk.Tk()
window.title('Event Binding')
window.geometry('800x500')

# widgets
text = tk.Text(window)
text.pack()

entry = ttk.Entry(window)
entry.pack()

btn = ttk.Button(window, text='A button')
btn.pack()

# events
btn.bind('<Alt-KeyPress-a>', lambda event: print('an event'))
# text.bind('<Motion>', get_pos)
window.bind('<KeyPress>', lambda event: print(f'{event.char}'))

entry.bind('<FocusIn>', lambda event: print('entry field was selected'))


window.mainloop()
