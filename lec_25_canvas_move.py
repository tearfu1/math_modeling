import tkinter as tk

def move_func():
    x=10
    y=10
    canvas.move(circle, x, y)
    window.after(50)

window = tk.Tk()

canvas = tk.Canvas()

canvas.pack()

circle = canvas.create_oval(10, 10, 30, 30, fill='black')

#canvas.after_idle(move_func) // чтоб само двигалось

sraka_motika = tk.Button(window, text='111', command=move_func)

sraka_motika.pack()

window.mainloop()