# *args allows a function to accept any number of positional arguments.
def student(name, *marks):
    print("Name : ", name)
    print("Marks: ", marks)
student("Raju", 50,35,45)

#No Arguments

def count_numbers(*args):
    print(len(args))
count_numbers()

# Python still creates the args tuple, but since there are no values, it becomes an empty tuple