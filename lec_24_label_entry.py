import tkinter as tk

window = tk.Tk()

entry_1 = tk.Entry(fg="yellow",
                   bg="black",
                   width=50)

name = entry_1.get()
entry_1.insert(0, "123 ")
entry_1.delete(0, 1)
entry_1.pack()

window.mainloop()