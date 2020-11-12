import tkinter as tk

window = tk.Tk()

canvas = tk.Canvas()

canvas.create_oval(10, 10, 80, 80, outline='#f11',
                   fill='white', width=2)

canvas.create_arc(10, 10, 80, 80, outline='#f11',
                   fill='red', width=2)
canvas.create_rectangle(150, 150, 180, 180, outline='#f11',
                   fill='white', width=2)

points = [150, 123, 241, 46, 78, 325, 212,63]

canvas.create_polygon(points, outline='#f11',
                   fill='white', width=2)

canvas.pack()

window.mainloop()