#   Charlie language
#
#   Vowels are transformed into c's

def translate(phrase):
    translation = ""

    for letter in phrase:
        if letter.lower() in "aeiou":
            if letter.isupper():
                translation = translation + "C"
            else:
                translation = translation + "c"
        else:
            translation = translation + letter

    return translation

print(translate(input("Enter a phrase: ")))