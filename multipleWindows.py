import tkinter as tk
from tkinter import ttk, messagebox

class Extra(tk.Toplevel):
    def __init__(self):
        super().__init__()
        self.title('extra window')
        self.geometry('700x600')
        ttk.Label(self, text='label').pack()
        ttk.Button(self, text='button').pack()
        ttk.Label(self, text=' 2').pack(expand=True)

def ask_yes_no():
    # answer = messagebox.askquestion('Question', 'Yes or no?')
    # print(answer)
    messagebox.showerror('Title', 'Body')

def create_window():
    global extra_window
    extra_window = Extra()
    # extra_window = tk.Toplevel()
    # extra_window.title('extra window')
    # extra_window.geometry('700x600')
    # ttk.Label(extra_window, text='label').pack()
    # ttk.Button(extra_window, text='button').pack()
    # ttk.Label(extra_window, text=' 2').pack(expand=True)

def close_window():
    extra_window.destroy()

window = tk.Tk()
window.title('Multiple Windows')
window.geometry('500x400+900+150')

button1 = ttk.Button(window, text='open main window', command=create_window)
button1.pack(expand=True)

button2 = ttk.Button(window, text='close main window', command=close_window)
button2.pack(expand=True)

button3 = ttk.Button(window, text='create yes or no window', command=ask_yes_no)
button3.pack(expand=True)








# run
window.mainloop()