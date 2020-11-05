import tkinter as tk

window = tk.Tk()

text_1 = tk.Label(text="hello world",bg="white", width=20)
label_1 = tk.Label(text="blok", 
                   bg="blue",
                   fg="red",
                   width=20,
                   height=20)
text_2 = tk.Label(text="hello world", bg="red",width=20)

text_1.pack()
label_1.pack()
text_2.pack()

window.mainloop()