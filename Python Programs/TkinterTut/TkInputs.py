from tkinter import *

root = Tk()

#   Field to input stuff
entry = Entry(root, width = 50)
entry.pack()
entry.insert(0, "Enter Your Name: ")

def MyClick():

    hello = "Hello " + entry.get()
    myLabel = Label(root,
                    text = hello)
    myLabel.pack()

myButton = Button(root,
                  text = "Enter Your Name!",
                  command = MyClick)
myButton.pack()

root.mainloop()