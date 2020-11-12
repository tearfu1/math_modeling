import tkinter as tk

window = tk.Tk()

canvas = tk.Canvas()

canvas.create_line(15, 25, 200, 25)
canvas.create_line(35, 35, 200, 25, dash=(4,2))
canvas.create_line(55, 85, 155, 85, 105, 180, 55, 85)

canvas.pack()

window = tk.mainloop()