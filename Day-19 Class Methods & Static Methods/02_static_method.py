# What is a Static Method?

# A static method belongs to the class, but it doesn't use:
# self
# cls
# It behaves like a normal function placed inside the class because it is related to that class.

class Calculator:

    @staticmethod
    def add(a, b):
        return a + b

print(Calculator.add(10, 20))
print(Calculator.add(50, 60))

# Notice:

# No object is created.
# No self.
# No cls.

class Student:

    @staticmethod
    def greet():
        print("Welcome to Python OOP")

Student.greet()