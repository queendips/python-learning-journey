# What is self?

# self represents the current object.
# Each object has its own copy of data.

class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age

student1 = Student("Dipali", 25)
student2 = Student("Rahul", 28)

print(student1.name)
print(student1.age)

print(student2.name)
print(student2.age)