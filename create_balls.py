import tkinter as tk
import numpy as np
from random import randint as rd

class Ball:
    
    def __init__(self, canvas, window, x1, y1, x2, y2):
        self.canvas = canvas
        self.window = window
        self.ball = self.canvas.create_oval(x1, y1, x2, y2)
        
    def interection(self):
        
        self.x = np.arange(0, 5, 0.01)
        self.y = np.sin(self.x)
        
        return self.x, self.y
    
    def move_ball(self, counter=0):
        if counter < len(self.interection()[0]):
            self.canvas.move(self.ball,
                             self.interection()[0][counter],
                             self.interection()[1][counter])
            self.window.after(10, lambda: self.move_ball(counter+1))

window = tk.Tk()
canvas = tk.Canvas(window, width=1000, height=600)
canvas.pack()

def create_func():
    x0 = rd(0, 400)
    y0 = rd(0, 400)
    radius = rd(10, 100)
    
    ball = Ball(canvas, window, 
                x1=x0-radius, y1=y0-radius, 
                x2=x0+radius, y2=y0+radius)
    
    ball.move_ball()

bt = tk.Button(window, text='tikni', command=create_func)
bt.pack()

window.mainloop()