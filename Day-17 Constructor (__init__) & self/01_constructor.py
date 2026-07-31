# Constructor Without Parameters
class Student:
    def __init__(self):
        print("Student object created")

student1 = Student()
student2 = Student()
student3 = Student() 

# Python does two things:

# Creates a new object.
# Automatically calls the constructor (__init__())

# Constructor With Parameters
class Student:
    def __init__(self, name):
        print("Welcome", name)
student1 = Student("Dipali")
student2 = Student("Rahul")