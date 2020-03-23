from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Tk New Window")
root.iconbitmap("tabicon.ico")
root.geometry("400x400")


ddbMenuOptions = [
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
    "Sunday"
]

ddbOption = StringVar()
#   Sets a default value
ddbOption.set(ddbMenuOptions[0])

def ShowOption():

    myLabel = Label(root, text = ddbOption.get()).pack()

#   Drop Down Boxes

ddbMenu = OptionMenu(root, ddbOption, *ddbMenuOptions)
ddbMenu.pack()

button = Button(root, text = "Show Selection", command = ShowOption)
button.pack()

root.mainloop()