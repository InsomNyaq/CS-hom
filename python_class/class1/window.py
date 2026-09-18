import tkinter as tk

window  =  tk.Tk()
window.title("Hello World --GUI")

label = tk.label(window,
                 text = "Hello World",
                 font = ("Arial",24),
                 fg = "red")

label.pack(pady=20)

window.mainloop()