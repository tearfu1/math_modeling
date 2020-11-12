import tkinter as tk
import numpy as np

t = np.arange
t = [0,0.1,0.2,0.3]

def time (t):
    t = t + 1

def move_func(t):
    x0=0
    y0=0
    vx0=5
    vy0=5
    gy=9.8
    
    x=x0+vx0*t
    y=y0+vy0*t-((gy*t**2)/2)
    print(x,y)
    canvas.move(circle, x, y)
    window.after(50)

window = tk.Tk()

canvas = tk.Canvas(width=600, height=600)

canvas.create_rectangle(0, 170, 50, 180, outline='#f11',
                   fill='white', width=2)

canvas.create_polygon(30, 170, 40, 150, 50, 160, 45, 170,
                   fill='black', width=2)

canvas.pack()

circle = canvas.create_oval(50, 150, 60, 160, fill='red')

#canvas.after_idle(move_func)

knopka = tk.Button(window, text='огонь', command=move_func)

knopka.pack()

window.mainloop()