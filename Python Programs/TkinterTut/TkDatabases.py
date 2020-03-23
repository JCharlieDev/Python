from tkinter import *
import sqlite3
from PIL import ImageTk, Image

root = Tk()
root.title("Tk New Window")
root.iconbitmap("tabicon.ico")
root.geometry("700x700")

#   Create or connect to a database
conn = sqlite3.connect('Databases\\address_book.db')
#   Create cursor instance
cursor = conn.cursor()

#   Create tables
'''
cursor.execute("""CREATE TABLE addresses (
    firstName text,
    lastName text,
    address text,
    city text,
    state text,
    zipcode integer
    )""")
'''

def Submit():

    #   Create or connect to a database
    conn = sqlite3.connect('Databases\\address_book.db')
    #   Create cursor instance
    cursor = conn.cursor()

    #   Insert into table
    cursor.execute("INSERT INTO addresses VALUES (:firstName, :lastName, :address, :city, :state, :zipCode)",
                   {
                       'firstName': firstName.get(),
                       'lastName': lastName.get(),
                       'address': address.get(),
                       'city': city.get(),
                       'state': state.get(),
                       'zipCode': zipCode.get()
                   })

    #   Clear the text boxes
    firstName.delete(0, END)
    lastName.delete(0, END)
    address.delete(0, END)
    city.delete(0, END)
    state.delete(0, END)
    zipCode.delete(0, END)

    #   Commit changes
    conn.commit()
    #   Close Connection
    conn.close()

#   Create Query function

def ShowRecords():

    printRecords = ''

    #   Create or connect to a database
    conn = sqlite3.connect('Databases\\address_book.db')
    #   Create cursor instance
    cursor = conn.cursor()

    #   Query the database

    cursor.execute("SELECT *, oid FROM addresses")
    records = cursor.fetchall()   #   Fecthes all reecords
    #   print(records)

    #   Loop through records
    for record in records:
        printRecords += str(record[0]) + " " + str(record[1]) + " " + "\t" + str(record[6]) + "\n"

    queryLabel = Label(root, text = printRecords)
    queryLabel.grid(row = 12, column = 0, columnspan = 2)

    #   Commit changes
    conn.commit()
    #   Close Connection
    conn.close()

#   Create Delete function

def Delete():

    #   Create or connect to a database
    conn = sqlite3.connect('Databases\\address_book.db')
    #   Create cursor instance
    cursor = conn.cursor()

    #   Delete record
    cursor.execute("DELETE from addresses WHERE oid = " + deleteBox.get())


    #   Commit changes
    conn.commit()
    #   Close Connection
    conn.close()

# Create Update button

def Update():

    #   Create or connect to a database
    conn = sqlite3.connect('Databases\\address_book.db')
    #   Create cursor instance
    cursor = conn.cursor()

    recordID = deleteBox.get()

    cursor.execute(""" UPDATE addresses SET
        firstName = :first,
        lastName = :last,
        address = :address,
        city = :city,
        state = :state,
        zipCode = :zipCode
    
        WHERE oid = :oid""",
                   {
                       'first': firstNameUpdate.get(),
                       'last': lastNameUpdate.get(),
                       'address': addressUpdate.get(),
                       'city': cityUpdate.get(),
                       'state': stateUpdate.get(),
                       'zipCode': zipCodeUpdate.get(),
                       'oid': recordID
                   })


    #   Commit Changes
    conn.commit()
    #   Close Connection
    conn.close()

    updateWindow.destroy()

#   Create new Window function

def UpdateWindow():

    global updateWindow

    updateWindow = Tk()
    updateWindow.title("Update Database Record")
    updateWindow.iconbitmap("tabicon.ico")
    updateWindow.geometry("700x700")

    printRecords = ''
    recordID = deleteBox.get()

    #   Create or connect to a database
    conn = sqlite3.connect('Databases\\address_book.db')
    #   Create cursor instance
    cursor = conn.cursor()

    #   Query the database

    cursor.execute("SELECT *, oid FROM addresses WHERE oid = " + recordID)
    records = cursor.fetchall()   #   Fecthes all reecords

    queryLabel = Label(root, text = printRecords)
    queryLabel.grid(row = 12, column = 0, columnspan = 2)

    #   Create Global variables for text box names

    global firstNameUpdate
    global lastNameUpdate
    global addressUpdate
    global cityUpdate
    global stateUpdate
    global zipCodeUpdate


    #   Create text boxes
    firstNameUpdate = Entry(updateWindow, width=30)
    firstNameUpdate.grid(row=0, column=1, padx=20, pady=(10, 0))

    lastNameUpdate = Entry(updateWindow, width=30)
    lastNameUpdate.grid(row=1, column=1)

    addressUpdate = Entry(updateWindow, width=30)
    addressUpdate.grid(row=2, column=1)

    cityUpdate = Entry(updateWindow, width=30)
    cityUpdate.grid(row=3, column=1)

    stateUpdate = Entry(updateWindow, width=30)
    stateUpdate.grid(row=4, column=1)

    zipCodeUpdate = Entry(updateWindow, width=30)
    zipCodeUpdate.grid(row=5, column=1)

    #   Create text box labels

    firstNameLabelUpdate = Label(updateWindow, text="First Name:")
    firstNameLabelUpdate.grid(row=0, column=0, pady=(10, 0))

    lastNameLabelUpdate = Label(updateWindow, text="Last Name:")
    lastNameLabelUpdate.grid(row=1, column=0)

    addressLabelUpdate = Label(updateWindow, text="Address:")
    addressLabelUpdate.grid(row=2, column=0)

    cityLabelUpdate = Label(updateWindow, text="City:")
    cityLabelUpdate.grid(row=3, column=0)

    stateLabelUpdate = Label(updateWindow, text="State:")
    stateLabelUpdate.grid(row=4, column=0)

    zipCodeLabelUpdate = Label(updateWindow, text="Zip Code:")
    zipCodeLabelUpdate.grid(row=5, column=0)

    #   Loop through results

    for record in records:
        firstNameUpdate.insert(0, record[0])
        lastNameUpdate.insert(0, record[1])
        addressUpdate.insert(0, record[2])
        cityUpdate.insert(0, record[3])
        stateUpdate.insert(0, record[4])
        zipCodeUpdate.insert(0, record[5])

    #   Create Update Button

    updateButton = Button(updateWindow, text="Save Record to Database", command= Update)
    updateButton.grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx=100)

#   Create text boxes
firstName = Entry(root, width = 30)
firstName.grid(row = 0, column = 1, padx = 20, pady = (10, 0))

lastName = Entry(root, width = 30)
lastName.grid(row = 1, column = 1)

address = Entry(root, width = 30)
address.grid(row = 2, column = 1)

city = Entry(root, width = 30)
city.grid(row = 3, column = 1)

state = Entry(root, width = 30)
state.grid(row = 4, column = 1)

zipCode = Entry(root, width = 30)
zipCode.grid(row = 5, column = 1)

deleteBox = Entry(root, width = 30)
deleteBox.grid(row = 8, column = 1)

#   Create text box labels

firstNameLabel = Label(root, text = "First Name:")
firstNameLabel.grid(row =0, column = 0, pady = (10, 0))

lastNameLabel = Label(root, text = "Last Name:")
lastNameLabel.grid(row =1, column = 0)

addressLabel = Label(root, text = "Address:")
addressLabel.grid(row =2, column = 0)

cityLabel = Label(root, text = "City:")
cityLabel.grid(row =3, column = 0)

stateLabel = Label(root, text = "State:")
stateLabel.grid(row =4, column = 0)

zipCodeLabel = Label(root, text = "Zip Code:")
zipCodeLabel.grid(row =5, column = 0)

deleteBoxLabel = Label(root, text = "ID Number to Delete ")
deleteBoxLabel.grid(row = 8, column = 0)

#   Create Submit Button

submitButton = Button(root, text = "Add Record to Database", command = Submit)
submitButton.grid(row = 6, column = 0, columnspan = 2, pady = 10, padx = 10, ipadx = 100)

#   Create Query Button

queryButton = Button(root, text = "Show Records", command = ShowRecords)
queryButton.grid(row = 7, column = 0, columnspan = 2, pady = 10, padx = 10, ipadx = 100)

#   Create Delete Button

deleteButton = Button(root, text = "Delete Records", command = Delete)
deleteButton.grid(row = 9, column = 0, columnspan = 2, pady = 10, padx = 10, ipadx = 100)

#   Create Update Button

updateButton = Button(root, text = "Edit Record", command = UpdateWindow)
updateButton.grid(row = 11, column = 0, columnspan = 2, pady = 10, padx = 10, ipadx = 100)

#   Commit changes
conn.commit()

#   Close Connection
conn.close()

root.mainloop()