# **kwargs allows a function to accept any number of keyword arguments.
# Instead of receiving values as a tuple (*args), Python stores keyword arguments in a dictionary.

def details (**kwargs):
    print("Name: ", kwargs["name"])
    print("City: ", kwargs["city"])
details(name = "Raju", city = "Pune" )

# Normal Parameter + **kwargs
def student(name, **kwargs):
    print("Name:", name)
    print("Other Details:", kwargs)

student("Bob", city="Kagpur", age=55)

# No Keyword Arguments

def details(**kwargs):
    print(kwargs)

details()