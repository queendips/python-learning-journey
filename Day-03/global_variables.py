# A global variable is a variable that is declared outside any function.
x = 10
def function():
    print(x)
function()

# Modifying a Global Variable
count = 0
def increment():
    global count #  tells Python to use the global variable instead of creating a local one.
    count = +1
increment()
print(count)