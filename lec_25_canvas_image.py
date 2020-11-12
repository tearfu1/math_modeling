import tkinter as tk
from PIL import Image, ImageTk

window = tk.Tk()

img = Image.open('22323.jpg')
meme = ImageTk.PhotoImage(img)
canvas = tk.Canvas(width=img.size[0]+20,
                   height=img.size[0]+20)

canvas.create_image(50, 50, image=meme)

canvas.pack()

window.mainloop()