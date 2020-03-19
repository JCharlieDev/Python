
#   "r" - reads, "w" - writes, "a" - append, "r+" reads and writes
employeeFile = open("C:/Users/MSI/Desktop/VideoGames Stuff/Programming Languages/Python/Python Programs/Basics/TestFiles/Employees.txt", "r")

#   returns if a file is readable
print(employeeFile.readable())

print(employeeFile.readline())
#   Reads next lines
print(employeeFile.readline())

#   Reads the lines and puts them in a list and we can index them
print(employeeFile.readlines()[1])

for emplyee in employeeFile.readlines():
    print(emplyee)

employeeFile.close()

