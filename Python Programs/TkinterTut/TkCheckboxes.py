from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Tk New Window")
root.iconbitmap("tabicon.ico")
root.geometry("400x400")

#   Tk variables are weird
chkVar = StringVar()   #   1 = Checked, 0 = not checked

#   Updates the label status of the checkbox
def IsChecked():

    myLabel = Label(root, text=chkVar.get()).pack()

chkButton = Checkbutton(root, text = "Would you like to Supersize your order?", variable = chkVar, onvalue = "Supersize", offvalue = "Regular Size")
chkButton.deselect()
chkButton.pack()

button = Button(root, text = "Show Selection", command = lambda : IsChecked()).pack()

root.mainloop()