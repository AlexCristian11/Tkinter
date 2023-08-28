import tkinter as tk
from PIL import Image
Image.CUBIC = Image.BICUBIC
import ttkbootstrap as ttk
from ttkbootstrap.scrolled import ScrolledFrame
from ttkbootstrap.toast import ToastNotification
from ttkbootstrap.tooltip import ToolTip
from ttkbootstrap.widgets import DateEntry, Floodgauge, Meter

window = ttk.Window(themename='darkly')
window.title('extra widgets')
window.geometry('500x700+700+100')

# scrollable frame
scroll_frame = ScrolledFrame(window)
scroll_frame.pack(expand=True, fill='both')

for i in range(100):
    frame = ttk.Frame(scroll_frame)
    ttk.Label(frame, text=f'Label: {i}').pack(fill='x', side='left')
    ttk.Button(frame, text=f'Button: {i}').pack(fill='x', side='left')
    frame.pack(fill='x', expand=True)

# toast
toast = ToastNotification(
    title='A toast',
    message='This is the actual message',
    duration=2000,
    bootstyle='danger',
    position=(10, 10, 'ne'))

ttk.Button(window, text='show toast', command=lambda : toast.show_toast()).pack()

# tooltip
button = ttk.Button(window, text='Tooltip text', bootstyle='warning')
button.pack(pady=10)
ToolTip(button, text='a tooltip', bootstyle='danger-inverse')

# calendar
calendar = DateEntry(window)
calendar.pack(pady=10)

button2 = ttk.Button(window, text='Get calendar date', command=lambda : print(calendar.entry.get()))
button2.pack(pady=10)

# progress bar
progress_int = tk.IntVar(value=50)
progress = ttk.Floodgauge(window, text='Progress', variable=progress_int, bootstyle='danger', mask='mask {}%')
progress.pack(pady=10, fill='x')
ttk.Scale(window, from_=0, to=100, variable=progress_int).pack()


# meter
meter = ttk.Meter(window, amounttotal=100, metersize=150, padding=5, amountused=25, metertype='semi', subtext='km per hour', interactive=True)
meter.pack(pady=20)

entry = ttk.Entry(window, textvariable=meter.amountusedvar)
entry.pack(pady=10)



# run
window.mainloop()
