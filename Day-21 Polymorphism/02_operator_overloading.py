# Python operators already work differently for different data types.
# Creating Your Own Operator Overloading
class Book:

    def __init__(self, pages):
        self.pages = pages

    def __add__(self, other):
        return self.pages + other.pages

book1 = Book(150)
book2 = Book(200)

print(book1 + book2)