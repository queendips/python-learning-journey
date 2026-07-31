# Parent Class
class Animal:

    def eat(self):
        print("Animal is eating")

# Child Class
class Dog(Animal):

    def bark(self):
        print("Dog is barking")

dog = Dog()

dog.eat()    # Inherited method
dog.bark()   # Own method

# Child Constructor
class Animal:

    def __init__(self):
        print("Animal Constructor")

class Dog(Animal):

    def __init__(self):
        print("Dog Constructor")

dog = Dog()
# The child constructor overrides the parent constructor.
# Calling Parent Constructor

# Use super().

class Animal:

    def __init__(self):
        print("Animal Constructor")

class Dog(Animal):

    def __init__(self):
        super().__init__()
        print("Dog Constructor")

dog = Dog()
# super() lets the child class call methods from the parent class.
