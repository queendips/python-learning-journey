# Public members can be accessed from anywhere.
class Student:

    def __init__(self, name):
        self.name = name

student = Student("Dipali")

print(student.name)

# name is a public attribute.