import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext

window = tk.Tk()
window.title('Sliders')
window.geometry('800x600')


# slider
scale_int = tk.IntVar(value=15)
scale = ttk.Scale(window,
                  command=lambda value: print(scale_int.get()),
                  from_=0, to=25,
                  length=300,
                  orient='horizontal',
                  variable=scale_int,
                  )
scale.pack()

# progress bar
progress = ttk.Progressbar(window,
                           variable=scale_int,
                           maximum=25,
                           mode='determinate',
                           length=400)
progress.pack()

# progress.start()

# scrolled text
scrolled_text = scrolledtext.ScrolledText(window, width=100, height=20)
scrolled_text.pack()

progress_var = tk.IntVar()
ex_scale = ttk.Scale(window, variable=progress_var, from_=0, to=100, command=lambda value: print(progress_var.get()))
ex_scale.pack()
ex_progress = ttk.Progressbar(window, orient='vertical', variable=progress_var)

ex_progress.start()
ex_progress.pack()

label = ttk.Label(window, textvariable=progress_var)
label.pack()


window.mainloop()
