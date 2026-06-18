# center()
# Centers the string within a specified width.
text = "Python"

print(text.center(20))

text = "Python"

print(text.center(20, "*"))
# ljust()
# Aligns the string to the left.
print(text.ljust(15, "-"))

# rjust()
# Aligns the string to the right.
print(text.rjust(15, "-"))

# zfill()
# Pads the string with zeros from the left.
number = "25"

print(number.zfill(5))


ticket = "123"

print(ticket.zfill(8))

# format()
# Formats values into a string.
# name = "Raju"
# age = 45

# print("My name is {} and I am {} years old".format(name, age))
print("Name: {0}, Age: {1}".format("Bob", 25))