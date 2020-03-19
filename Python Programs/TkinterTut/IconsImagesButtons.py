from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Imagaes, Buttons and Icons")
root.iconbitmap("tabicon.ico")

myImage = ImageTk.PhotoImage(Image.open("C:\\Users\MSI\\Documents\\GitHub Repos\\Portfolio\\Images\\PythonImagestest\\Briggite.jpg"))
myLabel = Label(image = myImage)
myLabel.pack()

buttonQuit = Button(root, text = "Exit", command = root.quit)



buttonQuit.pack()


root.mainloop()