# Multilevel Inheritance

# One class inherits from another, which inherits from another.

class Animal:

    def eat(self):
        print("Animal eats food")

class Mammal(Animal):

    def walk(self):
        print("Mammal walks")

class Dog(Mammal):

    def bark(self):
        print("Dog barks")

dog = Dog()

dog.eat()
dog.walk()
dog.bark()

# The Dog object can use methods from all levels.