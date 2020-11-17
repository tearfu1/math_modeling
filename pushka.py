import tkinter as tk
import numpy as np

window = tk.Tk()

x0 = 50
y0 = 150
R = 10

canvas = tk.Canvas(width=600, height=600)

canvas.create_rectangle(0, 170, 50, 180, outline='#f11',
                   fill='white', width=2)

canvas.create_line(0, 170,10000, 170)

canvas.create_polygon(30, 170, 40, 150, 50, 160, 45, 170,
                   fill='black', width=2)

canvas.pack()
    
ball = canvas.create_oval(x0-R,
                          y0-R,
                          x0+R,
                          y0+R,
                          fill='red')


t = np.arange(0, 100, 0.1)
x0=0
y0=0
vx0=10
vy0=-10
gy=9.8


def move_func():
    x_coords = x0+vx0*t
    y_coords = y0+vy0*t+((gy*t**2)/2)
    i=1   
    
    def reload ():
        x_coords[i] = 0
        y_coords[i] = 0
    while True:
        canvas.move(ball, x_coords[i], y_coords[i])
        window.update()
        window.after(100)
        i += 1

        if y_coords[i] >= 18:
            break 



button_reload = tk.Button(window, text='перезарядка', command=reload)
button_reload.pack()

knopka = tk.Button(window, text='огонь', command=move_func)
knopka.pack()


window.mainloop()
