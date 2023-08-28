import tkinter as tk
from tkinter import ttk
import customtkinter as ctk
try:
    from ctypes import windll, byref, sizeof, c_int
except:
    pass


app = ctk.CTk()
app.geometry('300x200+600+200')

# change the title bar color
try:
    HWND = windll.user32.GetParent(app.winfo_id())
    color = 0x000000FF
    title_color = 0x0000FF00
    windll.dwmapi.DwmSetWindowAttribute(HWND, 35, byref(c_int(color)), sizeof(c_int))
    windll.dwmapi.DwmSetWindowAttribute(HWND, 36, byref(c_int(title_color)), sizeof(c_int))
except:
    pass

app.mainloop()


# try and catch for machines not running on Windows
