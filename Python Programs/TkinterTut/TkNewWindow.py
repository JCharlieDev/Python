from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Tk New Window")
root.iconbitmap("tabicon.ico")

def OpenWindow():

    top = Toplevel()
    top.title("New window")
    top.iconbitmap("tabicon.ico")

    #   garbage collector gets rid of it if its not global
    global myImage

    myImage = ImageTk.PhotoImage(Image.open("C:\\Users\\MSI\\Documents\\GitHub Repos\\Portfolio\\Images\\PythonImagestest\\Sigma.jpg"))
    myLabel = Label(top, image=myImage).pack()

    buttonExit = Button(top, text = "Close", command = lambda : top.destroy()).pack()


button = Button(root, text = "Open New Window", command = lambda : OpenWindow())

button.pack()


mainloop()