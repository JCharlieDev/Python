
isMale = True
isTall = True

if isMale or isTall:
    print("You are a male or tall of both")
elif isMale and not(isTall):
    print("You are a short male")
elif not(isMale) and isTall:
    print("You are not a male but you are tall")
else:
    print("You are not a male and you are not tall")
