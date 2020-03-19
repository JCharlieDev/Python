#   Student class
class Student:

    def __init__(self, name, major, gpa, isOnProvation):
        self.name = name
        self.major = major
        self.gpa = gpa
        self.isOnProvation = isOnProvation

    def OnHonorRoll(self):
        if self.gpa >= 3.5:
            return True
        else:
            return False