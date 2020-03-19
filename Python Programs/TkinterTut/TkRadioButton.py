from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Tk Radio Buttons")
root.iconbitmap("tabicon.ico")

#rbVar1 = IntVar()


TOPPINGS = [
    ("Pepperoni", "Pepperoni"),
    ("Cheese", "Cheese"),
    ("Mushroom", "Mushroom"),
    ("Onion", "Onion")
]

pizza = StringVar()
pizza.set("Pepperoni")

for text, topping in TOPPINGS:
    Radiobutton(root, text = text, variable = pizza, value = topping).pack(anchor = W)

def RbClicked(value):

    myLabel = Label(root, text= value)
    myLabel.pack()

#   Radiobutton(root, text = "Option 1", variable = rbVar1, value = 1, command = lambda: RbClicked(rbVar1.get())).pack()
#   Radiobutton(root, text = "Option 2", variable = rbVar1, value = 2, command = lambda: RbClicked(rbVar1.get())).pack()

#   myLabel = Label(root, text = pizza.get())
#   myLabel.pack()

button = Button(root, text = "Click me", command = lambda : RbClicked(pizza.get()))
button.pack()

root.mainloop()