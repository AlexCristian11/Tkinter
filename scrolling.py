import tkinter as tk
from tkinter import ttk
from random import randint, choice


window = tk.Tk()
window.title('Scrolling')
window.geometry('500x400+900+150')


# canvas
# canvas = tk.Canvas(window, bg='orange', scrollregion=(0, 0, 2000, 5000))
# canvas.create_line(0, 0, 2000, 5000, fill='white', width=10)
# for i in range(100):
#     l = randint(0, 2000)
#     t = randint(0, 5000)
#     r = l + randint(10, 500)
#     b = t + randint(10, 500)
#     color = choice(('red', 'green', 'blue', 'black'))
#     canvas.create_rectangle(l, t, r, b, fill=color)
# canvas.pack(expand=True, fill='both')
#
# # mousewheel scrolling
# canvas.bind('<MouseWheel>', lambda event: canvas.yview_scroll(-int(event.delta / 60), "units"))
#
# # scrollbar
# scroller = ttk.Scrollbar(window, orient='vertical', command=canvas.yview)
# canvas.config(yscrollcommand=scroller.set)
# scroller.place(relx=1, rely=0, relheight=1, anchor='ne')
#
#
# scrollbar_bottom = ttk.Scrollbar(window, orient='horizontal', command=canvas.xview)
# canvas.config(xscrollcommand=scrollbar_bottom.set)
# scrollbar_bottom.place(relx=0, rely=1, relwidth=1, anchor='sw')
#
# canvas.bind('<Control MouseWheel>', lambda event: canvas.xview_scroll(-int(event.delta / 60), "units"))

# text = tk.Text(window)
# for i in range(1, 200):
#     text.insert(f'{i}.0', f'text: {i} \n')
# text.pack(expand=True, fill='both')
#
# scroll_text = ttk.Scrollbar(window, orient='vertical', command=text.yview)
# text.config(yscrollcommand=scroll_text.set)
# scroll_text.place(relx=1, rely=0, relheight=1, anchor='ne')

# treeview
table = ttk.Treeview(window, columns=(1,2), show='headings')
table.heading(1, text='First Name')
table.heading(2, text='Last Name')
first_names = ['Bob', 'Maria', 'Alex', 'James', 'Susan', 'Henry', 'Lisa', 'Anna', 'Lisa']
last_names = ['Smith', 'Brown', 'Wilson', 'Thomson', 'Cook', 'Taylor', 'Walker', 'Clark']
for i in range(100):
    table.insert(parent='', index=tk.END, values=(choice(first_names), choice(last_names)))
table.pack(expand=True, fill='both')


scroll_table = ttk.Scrollbar(window, orient='vertical', command=table.yview)
table.config(yscrollcommand=scroll_table.set)
scroll_table.place(relx=1, rely=0, relheight=1, anchor='ne')


# run
window.mainloop()
