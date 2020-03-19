import random

feetInMiles = 5200
metersInKilometers = 1000
beatles = ["John Lennon", "Paul McCartney", "George Harrison", "Ringo Star"]

def GetFileExt(fileName):
    return fileName[fileName.index(".") + 1:]

def RollDice(num):
    return random.randint(1, num)