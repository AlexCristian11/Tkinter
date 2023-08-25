import tkinter as tk
from tkinter import ttk


class App(tk.Tk):
    def __init__(self, start_size):
        super().__init__()
        self.title('Responsive Layouts')
        self.geometry(f'{start_size[0]}x{start_size[1]}+{start_size[2]}+{start_size[3]}')

        self.frame = ttk.Frame(self)
        self.frame.pack(expand=True, fill='both')

        size_notifier = SizeNotifier(self, {300: self.create_small_layout, 600: self.create_medium_layout,
                                            1200: self.create_large_layout})
        self.mainloop()

    def create_small_layout(self):
        self.frame.pack_forget()
        self.frame = ttk.Frame(self)
        ttk.Label(self.frame, text='Label 1', background='red').pack(expand=True, fill='both', padx=10, pady=10)
        ttk.Label(self.frame, text='Label 2', background='green').pack(expand=True, fill='both', padx=10, pady=10)
        ttk.Label(self.frame, text='Label 3', background='blue').pack(expand=True, fill='both', padx=10, pady=10)
        ttk.Label(self.frame, text='Label 4', background='yellow').pack(expand=True, fill='both', padx=10, pady=10)
        self.frame.pack(expand=True, fill='both')

    def create_medium_layout(self):
        self.frame.pack_forget()
        self.frame = ttk.Frame(self)
        self.frame.columnconfigure((0,1), weight=1, uniform='a')
        self.frame.rowconfigure((0,1), weight=1, uniform='a')
        self.frame.pack(expand=True, fill='both')

        ttk.Label(self.frame, text='Label 1', background='red').grid(column=0, row=0, sticky='nsew')
        ttk.Label(self.frame, text='Label 2', background='green').grid(column=1, row=0, sticky='nsew')
        ttk.Label(self.frame, text='Label 3', background='blue').grid(column=0, row=1, sticky='nsew')
        ttk.Label(self.frame, text='Label 4', background='yellow').grid(column=1, row=1, sticky='nsew')

    def create_large_layout(self):
        self.frame.pack_forget()

        self.frame = ttk.Frame(self)
        self.frame.columnconfigure((0,1,2,3), weight=1, uniform='a')
        self.frame.rowconfigure(0, weight=1, uniform='a')
        self.frame.pack(expand=True, fill='both')

        ttk.Label(self.frame, text='Label 1', background='red').grid(column=0, row=0, sticky='nsew', padx=10, pady=10)
        ttk.Label(self.frame, text='Label 2', background='green').grid(column=1, row=0, sticky='nsew', padx=10, pady=10)
        ttk.Label(self.frame, text='Label 3', background='blue').grid(column=2, row=0, sticky='nsew', padx=10, pady=10)
        ttk.Label(self.frame, text='Label 4', background='yellow').grid(column=3, row=0, sticky='nsew', padx=10, pady=10)




class SizeNotifier:
    def __init__(self, window, size_dict):
        self.window = window
        self.size_dict = {key: value for key, value in sorted(size_dict.items())}
        self.current_min_size = None
        self.window.bind('<Configure>', self.check)

        self.window.update()

        min_height = self.window.winfo_height()
        min_width = list(self.size_dict)[0]
        self.window.minsize = (min_width, min_height)

    def check(self, event):
        if event.widget == self.window:
            window_width = event.width
            checked_size = None

        for min_size in self.size_dict:
            delta = window_width - min_size
            if delta >= 0:
                checked_size = min_size

        if checked_size != self.current_min_size:
            self.current_min_size = checked_size
            self.size_dict[self.current_min_size]()


app = App((400,300,900,150))