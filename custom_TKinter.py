import tkinter as tk
import customtkinter as ctk
from tkinter import ttk


window = ctk.CTk()
window.title('CustomTkinter')
window.geometry('800x600+500+150')

# widgets

string_var = ctk.StringVar(value='a custom string')

label = ctk.CTkLabel(
    window,
    text='A ctk Label',
    fg_color=('blue', 'red'),
    text_color=('black', 'white'),
    corner_radius=10,
    textvariable=string_var)
label.pack()

button = ctk.CTkButton(
    window,
    text='A ctk button',
    fg_color='#ff0',
    text_color='#000',
    hover_color='#AA0',
    command=lambda: ctk.set_appearance_mode('light'))
button.pack()

frame = ctk.CTkFrame(window, fg_color='transparent')
frame.pack()

slider = ctk.CTkSlider(frame)
slider.pack(padx=20, pady=20)

# exercise
switch = ctk.CTkSwitch(
    window,
    text='exercise switch',
    fg_color='red',
    progress_color='pink',
    button_color='green',
    button_hover_color='yellow',
    switch_width=60,
    switch_height=30,
    corner_radius=2)
switch.pack()

# run
window.mainloop()
