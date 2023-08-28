import tkinter as tk
from tkinter import ttk
import customtkinter as ctk
from PIL import Image, ImageTk


def stretch_image(event):
    global resized_tk
    # size
    width = event.width
    height = event.height

    # create image
    resized_image = image_original.resize((width, height))
    resized_tk = ImageTk.PhotoImage(resized_image)

    # place on canvas
    canvas.create_image(0, 0, image=resized_tk, anchor='nw')


def fill_image(event):
    global resized_tk

    # current ratio
    canvas_ratio = event.width / event.height

    # get coordinates
    if canvas_ratio > image_ratio:
        width = int(event.width)
        height = int(width / image_ratio)
    else:
        height = int(event.height)
        width = int(height * image_ratio)

    resized_image = image_original.resize((width, height))
    resized_tk = ImageTk.PhotoImage(resized_image)
    canvas.create_image(int(event.width / 2), int(event.height / 2), anchor='center', image=resized_tk)

window = tk.Tk()
window.geometry('800x600+400+100')
window.title('Images')

# grid layout
window.columnconfigure((0, 1, 2, 3), weight=1, uniform='a')
window.rowconfigure(0, weight=1)


# import an image
image_original = Image.open('images/david-clode-vb-3qEe3rg8-unsplash.jpg')
image_ratio = image_original.size[0] / image_original.size[1]
image_tk = ImageTk.PhotoImage(image_original)

python_dark = Image.open('images/570-5708783_logo-python-python-logo-clipart-4148354802.png').resize((30, 30))
python_dark_tk = ImageTk.PhotoImage(python_dark)

img_ctk = ctk.CTkImage(
    light_image=Image.open('images/570-5708783_logo-python-python-logo-clipart-4148354802.png').resize((30, 30)),
    dark_image=Image.open('images/Python_icon-icons.png').resize((30, 30)))

# widget
# label = ttk.Label(window, text='python', image=image_tk)
# label.pack()

button_frame = ttk.Frame(window)
button = ttk.Button(button_frame, text='    A button', image=python_dark_tk, compound='left')
button.pack(pady=10)

button_ctk = ctk.CTkButton(button_frame, text='    A button', image=img_ctk, compound='left')
button_ctk.pack(pady=10)

button_frame.grid(column=0, row=0, sticky='nsew')

# canvas
canvas = tk.Canvas(window, background='black', bd=0, highlightthickness=0, relief='ridge')
canvas.grid(column=1, columnspan=3, row=0, sticky='nsew')
canvas.bind('<Configure>', fill_image)

# run
window.bind('<Escape>', lambda event: window.quit())
window.mainloop()
