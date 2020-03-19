
luckyNumbers = [4, 8, 15, 16, 23, 42]
friends = ["Kevin", "Karen", "Jim", "Oscar", "Toby"]

#   Adds a list to the list
friends.extend(luckyNumbers)
#   Adds an element to the list
friends.append("Creed")
#   Inserts an element
friends.insert(1, "Allen")
#   Removes an element
friends.remove("Jim")

luckyNumbers.sort()

print(luckyNumbers)