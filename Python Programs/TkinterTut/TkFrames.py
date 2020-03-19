from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Tk Frames")
root.iconbitmap("tabicon.ico")

frame = LabelFrame(root, text = "This is my frame", padx = 50,  pady = 50)
frame.pack(padx = 10, pady = 10)

button = Button(frame, text = " Some button")
button1 = Button(frame, text = " Some other button")

button.grid(row = 0, column = 0)
button1.grid(row = 1, column = 1)


root.mainloop()