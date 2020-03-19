from tkinter import *
#   Mostly everything is a widget

#   Main Window
root = Tk()
#   Creating label widget
myLabel1 = Label(root, text = "Hello world")
myLabel2 = Label(root, text = "My name is Charlie")
#   Putting it on the screen
myLabel1.grid(row = 0, column = 0)
myLabel2.grid(row = 1, column = 5)


#   Event loop, loops the application to stay open
root.mainloop()