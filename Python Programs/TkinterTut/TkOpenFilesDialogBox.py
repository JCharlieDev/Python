from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog

root = Tk()
root.title("Tk New Window")
root.iconbitmap("tabicon.ico")

def OpenFile():

    global myImage

    #   We need to read the file first
    root.filename = filedialog.askopenfilename(
        initialdir="C:\\Users\\MSI\\Documents\\GitHub Repos\\Portfolio\\Images\\PythonImagestest",
        title="Select A File", filetype=(("jpg files", "*.jpg"), ("All Files", "*.*"), ("Suk dic", "*.dic")))

    myLabel = Label(root, text=root.filename).pack()
    myImage = ImageTk.PhotoImage(Image.open(root.filename))
    myImageLabel = Label(root, image=myImage).pack()


button = Button(root, text = "Open File", comman = lambda : OpenFile()).pack()

root.mainloop()