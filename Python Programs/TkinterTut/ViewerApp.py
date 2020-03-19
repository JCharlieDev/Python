from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Images, Buttons and Icons")
root.iconbitmap("tabicon.ico")

def Forward(nextImage):

    global myLabel
    global buttonForward
    global buttonBack

    #   Gets rir of the image
    myLabel.grid_forget()

    myLabel = Label(image = imageList[nextImage - 1])

    buttonForward = Button(root, text = ">>", command = lambda: Forward(nextImage + 1))
    buttonBack = Button(root, text = "<<", command = lambda: Back(nextImage - 1))

    if nextImage == 4:
        buttonForward = Button(root, text = ">>", state = DISABLED)

    myLabel.grid(row=0, column=0, columnspan=3)
    buttonBack.grid(row=1, column=0)
    buttonForward.grid(row=1, column=2)

    status = Label(root, text="Image " + str(nextImage) + " of " + str(len(imageList)), bd=1, relief=SUNKEN, anchor=E)
    status.grid(row=2, column=0, columnspan=3, sticky=W + E)

def Back(previousImage):

    global myLabel
    global buttonForward
    global buttonBack

    myLabel.grid_forget()

    myLabel = Label(image=imageList[previousImage - 1])

    buttonForward = Button(root, text=">>", command=lambda: Forward(previousImage + 1))
    buttonBack = Button(root, text="<<", command=lambda: Back(previousImage - 1))

    if previousImage == 1:
        buttonBack = Button(root, text = "<<", state = DISABLED)

    myLabel.grid(row=0, column=0, columnspan=3)
    buttonBack.grid(row=1, column=0)
    buttonForward.grid(row=1, column=2)

    status = Label(root, text="Image " + str(previousImage) + " of " + str(len(imageList)), bd=1, relief=SUNKEN, anchor=E)
    status.grid(row=2, column=0, columnspan=3, sticky=W + E)

myImage1 = ImageTk.PhotoImage(Image.open("C:\\Users\\MSI\\Documents\\GitHub Repos\\Portfolio\\Images\\PythonImagestest\\Briggite.jpg"))
myImage2 = ImageTk.PhotoImage(Image.open("C:\\Users\\MSI\\Documents\\GitHub Repos\\Portfolio\\Images\\PythonImagestest\\Sigma.jpg"))
myImage3 = ImageTk.PhotoImage(Image.open("C:\\Users\\MSI\\Documents\\GitHub Repos\\Portfolio\\Images\\PythonImagestest\\Tracer.jpg"))
myImage4 = ImageTk.PhotoImage(Image.open("C:\\Users\\MSI\\Documents\\GitHub Repos\\Portfolio\\Images\\PythonImagestest\\Widowmaker.jpg"))

imageList = [myImage1, myImage2, myImage3, myImage4]

status = Label(root, text = "Image 1 of " + str(len(imageList)), bd = 1, relief = SUNKEN, anchor = E)

myLabel = Label(image = myImage1)

myLabel.grid(row =0, column = 0, columnspan = 3)

#   BUTTONS
buttonBack = Button(root, text = "<<", command = Back, state = DISABLED)
buttonExit = Button(root, text = "Exit", command = root.quit)
buttonForward = Button(root, text = ">>", command = lambda: Forward(2))

buttonBack.grid(row = 1, column =0)
buttonExit.grid(row = 1, column =1)
buttonForward.grid(row = 1, column =2, pady = 10)
status.grid(row = 2, column = 0, columnspan = 3, sticky = W+E)


root.mainloop()