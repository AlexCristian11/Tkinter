import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.title('Canvas')
window.geometry('800x500')

# canvas
canvas = tk.Canvas(window, bg='white')
canvas.pack()

# canvas.create_rectangle((50, 20, 100, 200), fill='red', width=10, outline='green')
# canvas.create_oval((200,20,100,100), fill='blue')
# canvas.create_line(0, 0, 100, 156)
# # canvas.create_polygon((0,0, 100,200, 300,50), fill='pink')
# canvas.create_arc((200,20,100,100), fill='red', start=45, style=tk.ARC, outline='yellow', width=10)

# canvas.create_text((100, 200), text='this is a text', fill='green')
#
# canvas.create_window((50, 100), window=ttk.Button(window, text='text in a canvas'))

def draw_on_canvas(event):
    x = event.x
    y = event.y
    canvas.create_oval((x - brush_size / 2, y - brush_size / 2, x + brush_size / 2, y + brush_size / 2), fill='black')

def brush_size_adjust(event):
    global brush_size
    if event.delta > 0:
        brush_size += 4
    else:
        brush_size -= 4

    brush_size = max(0, min(brush_size, 50))


brush_size = 3
canvas.bind('<Motion>', draw_on_canvas)
canvas.bind('<MouseWheel>', brush_size_adjust)


# run
window.mainloop()
