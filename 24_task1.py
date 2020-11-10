import tkinter as tk
import random as rt

window = tk.Tk()

window.rowconfigure(0, minsize=50, weight=1)
window.columnconfigure([0, 1], minsize=50, weight=1)

label_1 = tk.Label(master=window, text="0")
label_1.grid(row=0, column=0)

def random():
    val = rt.randint(1,6)
    label_1['text'] = '{}'.format(val)

button_1 = tk.Button(master=window, text = "Бросить", command=random)

button_1.grid(row=0, column=1, sticky='nsew')
window.mainloop()