# What is Method Overriding?

# When a child class defines a method with the same name as a method in the parent class, the child's method replaces (overrides) the parent's version.

class Animal:

    def sound(self):
        print("Animal makes a sound")

class Dog(Animal):

    def sound(self):
        print("Dog barks")

dog = Dog()

dog.sound()
# Even though Dog inherits from Animal, its own sound() method is called.
# Calling the Parent Method

# Sometimes you want to execute both the parent and child methods.

class Animal:

    def sound(self):
        print("Animal makes a sound")

class Dog(Animal):

    def sound(self):
        super().sound()
        print("Dog barks")

dog = Dog()

dog.sound()

# super().sound() calls the parent class's method.