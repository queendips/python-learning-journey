# First-Class Function is a property of Python functions, not a special type of function.
# A First-Class Function is a function that can be:
# 1. Stored in a variable
# 2. Passed as an argument to another function
# 3. Returned from another function

# Python treats functions like any other object, such as numbers, strings, and lists.

# 1. Stored in a Variable
def greet():
    print("Hello")

message = greet #we are not calling the function we are storing in variable message.
message()

# 2. Passed as an Argument
def display(name):
    print(name)
display("Raju")
#-------------------
def tea():
    print("Making Tea")

def coffee():
    print("Making Coffee")
def make_drink(drink):
    drink()
make_drink(tea)
make_drink(coffee)