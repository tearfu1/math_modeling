import tkinter as tk

window = tk.Tk()

frame = tk.Frame(
                master=window,
                width=150,
                height=150
)
frame.pack()

label_1 = tk.Label(
                    master=frame,
                    text="adasd",
                    bg="red"
)
label_1.place(
            x=0,
            y=0
)
label_2 = tk.Label(
                    master=frame,
                    text="123123",
                    bg="green"
)
label_2.place(
            x=75,
            y=75
)

button_1 = tk.Button(
                    text="prikol",
                    bg="black",
                    fg="red"
)
button_1.place(x=10, y=10)

window.mainloop()