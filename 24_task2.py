import tkinter as tk

window = tk.Tk()

frame = tk.Frame(master=window,
                width=200,
                height=200)
frame.pack()

entry_1 = tk.Entry(master=frame,
                    fg="yellow",
                    bg="black",
                    width=7)
entry_1.place(x=0,y=0)

label_K_0 = tk.Label(text="K",
                    bg="black",
                    fg="red")
label_K_0.place(x=50, y=0)

label_K_1 =tk.Label(text="",
                    bg="black",
                    fg="red")
label_K_1.place(x=85, y=0)

label_K_C =tk.Label(text="C",
                    bg="black",
                    fg="red")
label_K_C.place(x=150, y=0)

def converter_K():
    name_K = entry_1.get()
    label_K_1['text'] = '{}'.format(int(name_K)-273,15)
    
button_K = tk.Button(text=">",
                    bg="black",
                    fg="red",
                    command=converter_K)
button_K.place(x=65, y=0)
#--------------------------------------------------------- vtoraya stroka
entry_2 = tk.Entry(master=frame,
                    fg="yellow",
                    bg="black",
                    width=7)
entry_2.place(x=0,y=50)

label_C_0 = tk.Label(text="C",
                    bg="black",
                    fg="red")
label_C_0.place(x=50, y=50)

label_C_1 =tk.Label(text="",
                    bg="black",
                    fg="red")
label_C_1.place(x=85, y=50)

label_C_K =tk.Label(text="K",
                    bg="black",
                    fg="red")
label_C_K.place(x=150, y=50)

def converter_C():
    name_C = entry_2.get()
    label_C_1['text'] = '{}'.format(int(name_C)+273,15)
    
button_C = tk.Button(text=">",
                    bg="black",
                    fg="red",
                    command=converter_C)
button_C.place(x=65, y=50)

window.mainloop()