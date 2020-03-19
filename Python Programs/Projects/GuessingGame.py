secretWord = "Giraffe"
guess = ""
guessCount = 0
guessLimit = 3
isOutOfGuesses = False

#   false in while loop exits the loop
while guess != secretWord and not(isOutOfGuesses):

    if guessCount < guessLimit:
        guess = input("Enter guess: ")
        guessCount += 1
    else:
        isOutOfGuesses = True

if isOutOfGuesses:
    print("Out of guesses, you lose")
else:
    print("You won!")