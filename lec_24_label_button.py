import tkinter as tk

window = tk.Tk()

button_1 = tk.Button(text="zhe4",
                     width=25,
                     height=5,
                     bg="blue",
                     fg="yellow")
button_1.pack()
button_2 = tk.Button(text="moskaley",
                     width=25,
                     height=5,
                     bg="yellow",
                     fg="blue")
button_2.pack()

window.mainloop()