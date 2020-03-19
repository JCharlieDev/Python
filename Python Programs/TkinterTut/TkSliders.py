from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Tk New Window")
root.iconbitmap("tabicon.ico")

#   Sets the size of the app window
root.geometry("400x400")

def Slide():

    myHorizontalLabel = Label(root, text=horizontal.get()).pack()

    root.geometry(str(horizontal.get()) + "x" + str(vertical.get()))

#   Slider widget
vertical = Scale(root, from_ = 0, to = 200)
vertical.pack()

horizontal = Scale(root, from_ = 0, to = 400, orient = HORIZONTAL)
horizontal.pack()

button = Button(root, text = "Click Me!", command = lambda : Slide()).pack()

root.mainloop()