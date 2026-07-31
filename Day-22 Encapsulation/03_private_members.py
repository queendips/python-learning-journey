# Private members start with double underscores.
# Python makes them harder to access directly through name mangling.
# class Employee:

#     def __init__(self, salary):
#         self.__salary = salary

# emp = Employee(50000)

# print(emp.__salary)

# output
# AttributeError:
# 'Employee' object has no attribute '__salary'
# Python internally changes:
# __salary
# to
# _Employee__salary
# This process is called name mangling.

# Accessing a Private Variable

class Employee:

    def __init__(self, salary):
        self.__salary = salary

emp = Employee(50000)

print(emp._Employee__salary)

# This works because Python internally renamed the variable.
# However, it's better to access private data through methods.