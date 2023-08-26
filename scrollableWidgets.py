import tkinter as tk
from tkinter import ttk


class ListFrame(ttk.Frame):
    def __init__(self, parent, text_data, item_height):
        super().__init__(parent)
        self.pack(expand=True, fill='both')

#       widget data
        self.text_data = text_data
        self.item_number = len(text_data)
        self.list_height = self.item_number * item_height

#       canvas
        self.canvas = tk.Canvas(self, background='red', scrollregion=(0, 0, 500, self.list_height))
        self.canvas.pack(expand=True, fill='both')

#       display frame
        self.frame = ttk.Frame(self)

        for index, item in enumerate(self.text_data):
            self.create_item(index, item).pack(expand=True, fill='both', pady=4, padx=10)

        self.canvas.create_window(
            (0, 0),
            window=self.frame,
            anchor='nw',
            width=500,
            height=400)

    def create_item(self, index, item):
        frame = ttk.Frame(self.frame)

#       grid layout
        frame.rowconfigure(0, weight=1)
        frame.columnconfigure((0, 1, 2, 3, 4), weight=1, uniform='a')

#       widgets
        ttk.Label(frame, text=f'#{index}').grid(row=0, column=0)
        ttk.Label(frame, text=f'#{item[0]}').grid(row=0, column=1)
        ttk.Button(frame, text=f'#{item[1]}').grid(row=0, column=2, columnspan=3, sticky='nsew')


window = tk.Tk()
window.title('Scrollable widgets')
window.geometry('500x400+900+150')

text_list = [('label', 'button'), ('thing', 'click'),
             ('third', 'something'), ('label1', 'button1'),
             ('label2', 'button2')]
list_frame = ListFrame(window, text_list, 100)

# run
window.mainloop()
