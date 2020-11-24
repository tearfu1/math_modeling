import tkinter as tk
import numpy as np
from random import randint as rd

window = tk.Tk()



canvas = tk.Canvas(width=1600, height=600)

canvas.create_rectangle(0, 170, 50, 180, outline='#f11',
                   fill='white', width=2)

canvas.create_line(0, 170,10000, 170)

canvas.create_polygon(30, 170, 40, 150, 50, 160, 45, 170,
                   fill='black', width=2)

canvas.pack()
    






def move_func():
    t = np.arange(0, 100, 0.1)
    x0=0
    y0=0
    vx0=rd(1,11) 
    vy0=-10
    gy=9.8
    
    x_coords = x0+vx0*t
    y_coords = y0+vy0*t+((gy*t**2)/2)
    i=1   

    R = 10
    ball = canvas.create_oval(50-R,
                          150-R,
                          50+R,
                          150+R,
                          fill='red')
    while True:
        canvas.move(ball, x_coords[i], y_coords[i])
        window.update()
        window.after(25)
        i += 1

        if y_coords[i] >= 17.5:
#            print('i ', y_coords)
#            print('i-1 ', y_coords[i-1])
            
            break 

knopka = tk.Button(window, text='огонь', command=move_func)
knopka.pack()


window.mainloop()