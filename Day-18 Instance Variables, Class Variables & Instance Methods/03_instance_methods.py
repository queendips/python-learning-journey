class Student:

    college = "ABC Engineering College"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print("Name :", self.name)
        print("Age :", self.age)
        print("College :", Student.college)

student1 = Student("Dipali", 32)
student2 = Student("Rahul", 28)

student1.display()

print()

student2.display()