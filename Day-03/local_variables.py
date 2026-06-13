# A local variable is a variable that is created inside a function.

# It can only be used within that function.
def greet():
    msg = "Hey hii!!"
    print(msg)
greet()

# Same Local Variable Name in Different Functions

def function1():
    x = 10
    print(x)
def function2():
    x =20
    print(x)
function1()
function2()