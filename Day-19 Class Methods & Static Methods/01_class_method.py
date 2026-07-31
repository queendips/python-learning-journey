# What is a Class Method?

# A class method works with class variables instead of object variables.
# It is created using the @classmethod decorator.
# The first parameter is cls (class).

# Syntax==>
# class Student:

#     @classmethod
#     def method_name(cls):
#         pass

class Student:

    college = "ABC Engineering College"

    def __init__(self, name):
        self.name = name

    @classmethod
    def change_college(cls, new_college):
        cls.college = new_college

student1 = Student("Dipali")
student2 = Student("Rahul")

print(student1.college)
print(student2.college)

Student.change_college("XYZ University")

print(student1.college)
print(student2.college)

# cls
# refers to the class itself, not an object.