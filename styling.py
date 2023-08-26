import tkinter as tk
from tkinter import ttk, font


window = tk.Tk()
window.title('Styling')
window.geometry('500x400+900+150')

# style
style = ttk.Style()
# print(style.theme_names())
# style.theme_use('vista')

style.configure('new.TButton', foreground='green', font=('', 20))
style.map('new.TButton',
          foreground=[('pressed', 'red'), ('disabled', 'yellow')],
          background=[('pressed', 'green'), ('active', 'blue')])

style.configure('TFrame', background='pink')

# widgets
label = ttk.Label(
    window,
    text='Label\nanother line',
    background='red',
    foreground='white',
    font=('Jokerman', 20),
    justify='center')
label.pack()

button = ttk.Button(window, text='Button', style='new.TButton')
button.pack()

# exercise
frame = ttk.Frame(window, height=200, width=100, style='TFrame')
frame.pack()



# run
window.mainloop()
