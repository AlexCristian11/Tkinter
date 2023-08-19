import tkinter as tk
from tkinter import ttk
from random import choice

window = tk.Tk()
window.title('Treeview')
window.geometry('800x500')


# data
first_names = ['Bob', 'Maria', 'Alex', 'James', 'Susan', 'Henry', 'Lisa', 'Anna', 'Lisa']
last_names = ['Smith', 'Brown', 'Wilson', 'Thomson', 'Cook', 'Taylor', 'Walker', 'Clark']


# treeview
table = ttk.Treeview(window, columns=('first', 'last', 'email'), show='headings')
table.heading('first', text='Firstname')
table.heading('last', text='Surname')
table.heading('email', text='Email')
table.pack(fill='both', expand=True)

# insert values
table.insert(parent='', index=0, values=('Joe', 'Doe', 'johndoe@email.com'))
for i in range(100):
    first = choice(first_names)
    last = choice(last_names)
    email = f'{first[0].lower()}{last.lower()}@email.com'
    data = (first, last, email)
    table.insert(parent='', index=0, values=data)

table.insert(parent='', index=tk.END, values=('xxxx', 'yyyy', 'zzzz'))


# events
def item_selector(_):
    print(table.selection())
    for i in table.selection():
        print(table.item(i)['values'])


def delete_items(_):
    for i in table.selection():
        table.delete(i)


table.bind('<<TreeviewSelect>>', item_selector)
table.bind('<Delete>', delete_items)


window.mainloop()
