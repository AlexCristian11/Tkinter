import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.title('More on window')
window.geometry('800x500+350+150')
window.iconbitmap('alert.ico')

# window sizes
window.minsize(200, 100)
# window.maxsize(1000, 700)
# window.resizable(True, False)

# screen attributes
print(window.winfo_screenwidth())
print(window.winfo_screenheight())


# window attributes
window.attributes('-alpha', 0.7)
window.attributes('-topmost', True)


# security event
window.bind('<Escape>', lambda event: window.quit())

# window.attributes('-disable', True)
# window.attributes('-fullscreen', True)

# title bar
# window.overrideredirect(True)
grip = ttk.Sizegrip(window)
grip.place(relx=1.0, rely=1.0, anchor='se')
grip.pack()

window.mainloop()
