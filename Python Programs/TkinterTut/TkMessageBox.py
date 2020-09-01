from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox

root = Tk()
root.title("Tk Radio Buttons")
root.iconbitmap("tabicon.ico")

def Popup():

    response = messagebox.showinfo("Some Message Box", "Usuario agregado con exito!")
    Label(root, text = response).pack()

    if response == 1:
        Label(root, text = "You clicked Yes!").pack()
    else:
        Label(root, text = "You clicked No...").pack()

Button(root, text = "Popup", command = lambda: Popup()).pack()



root.mainloop()