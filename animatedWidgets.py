import tkinter as tk
import customtkinter as ctk
from random import choice


class SlidePanel(ctk.CTkFrame):
    def __init__(self, parent, start_pos, end_pos):
        super().__init__(parent)

#         general attributes
        self.start_pos = start_pos + 0.04
        self.end_pos = end_pos - 0.02
        self.width = abs(start_pos - end_pos)
        self.place(relx=self.start_pos, rely=0.05, relwidth=self.width, relheight=.9)

#         animation logic
        self.pos = self.start_pos
        self.in_start_pos = True

    def animate(self):
        if self.in_start_pos:
            self.animate_forward()
        else:
            self.animate_backwards()

    def animate_forward(self):
        if self.pos > self.end_pos:
            self.pos -= 0.008
            self.place(relx=self.pos, rely=0.05, relwidth=self.width, relheight=.9)
            self.after(10, self.animate_forward)
        else:
            self.in_start_pos = False

    def animate_backwards(self):
        if self.pos < self.start_pos:
            self.pos += 0.008
            self.place(relx=self.pos, rely=0.05, relwidth=self.width, relheight=.9)
            self.after(10, self.animate_backwards)
        else:
            self.in_start_pos = True
# def move_button():
#     global button_x
#     button_x += 0.05
#     button.place(relx=button_x, rely=.5, anchor='center')
#     if button_x < 0.9:
#         window.after(10, move_button())
#
# #   configure
# #     colors = ['red', 'yellow', 'pink', 'green', 'orange']
# #     color = choice(colors)
# #     button.configure(fg_color=color)
#
#
# def animate():
#     global button_x
#     button_x += 0.5
#     if button_x < 10:
#         window.after(10, animate())


window = ctk.CTk()
window.title('Animated widgets')
window.geometry('800x600+500+100')
# ctk.set_appearance_mode('light')

# animated widgets
animated_panel = SlidePanel(window, 1, 0.7)
label1 = ctk.CTkLabel(animated_panel, text='Label 1')
label1.pack(expand=True, fill='both', padx=2, pady=10)

label2 = ctk.CTkLabel(animated_panel, text='Label 2')
label2.pack(expand=True, fill='both', padx=2, pady=10)

button1 = ctk.CTkButton(animated_panel, text='Button', corner_radius=0)
button1.pack(expand=True, fill='both', pady=10)

textbox = ctk.CTkTextbox(animated_panel, fg_color=('#dbdbdb', '#2b2b2b'))
textbox.pack(expand=True, fill='both', pady=10)


# button
button_x = 0.5
button = ctk.CTkButton(window, text='Toggle sidebar', command=animated_panel.animate)
button.place(relx=button_x, rely=.5, anchor='center')


# run
window.mainloop()
