import screen_brightness_control as sbc
from tkinter import *

root = Tk()
root.geometry("400x300")
root.title("Monitor Brightness Control")

# Obtener lista de monitores
monitors = sbc.list_monitors()
selected_monitor = StringVar(value=monitors[0] if monitors else "")

current_brightness = sbc.get_brightness(selected_monitor.get()) if monitors else 0
v1 = DoubleVar(value=current_brightness)

def update_brightness():
    monitor = selected_monitor.get()
    brightness = int(v1.get())
    sbc.set_brightness(brightness, display=monitor)
    l_status.config(text=f"Brillo: {brightness}%")

def select_monitor(monitor):
    selected_monitor.set(monitor)
    brightness = sbc.get_brightness(monitor)
    v1.set(brightness)
    l_status.config(text=f"Monitor: {monitor} - Brillo: {int(brightness)}%")

# Frame para botones
frame_buttons = Frame(root)
frame_buttons.pack(pady=10)

Label(frame_buttons, text="Selecciona Monitor:").pack()

for monitor in monitors:
    btn = Button(frame_buttons, text=monitor, command=lambda m=monitor: select_monitor(m),
                 bg="lightblue", width=20)
    btn.pack(pady=5)

# Frame para slider
frame_slider = Frame(root)
frame_slider.pack(pady=20)

Label(frame_slider, text="Ajusta Brillo:").pack()

s1 = Scale(frame_slider, variable=v1, from_=1, to=100, orient=HORIZONTAL,
           length=200, command=lambda x: update_brightness())
s1.pack()

# Etiqueta de estado
l_status = Label(root, text=f"Monitor: {selected_monitor.get()}", font=("Courier", 10))
l_status.pack(pady=10)

root.mainloop()
