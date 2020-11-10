import tkinter as tk

window = tk.Tk()

button_1 = tk.Button(text = "tikni",
                     width=50,
                     height=50,
                     fg="blue")

button_1.pack()

def click_left_mouse(event):
    print("left_mouse was clicked")
    
def click_right_mouse(event):
    print("right_mouse was clicked")
    
button_1.bind("<Button-1>", click_left_mouse)
button_1.bind("<Button-3>", click_right_mouse)

window.mainloop()


    