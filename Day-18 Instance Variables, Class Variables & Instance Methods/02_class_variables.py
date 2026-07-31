class Student:

    college = "ABC Engineering College"

    def __init__(self, name):
        self.name = name

student1 = Student("Dipali")
student2 = Student("Rahul")

print(student1.name)
print(student1.college)

print(student2.name)
print(student2.college)